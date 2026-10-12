import landPoints from "./land-points.json";
/**
 * V4 canvas adapter: geometry and imperative canvas controls are local to one mount.
 * React owns page sections; this renderer never handles financial records or network I/O.
 * @param {HTMLElement} root
 * @returns {() => void}
 */
export function initializeGlobe(root) {
  const $ = (selector) => root.querySelector(selector),
    $$ = (selector) => Array.from(root.querySelectorAll(selector));
  let disposed = false;
  const controller = new AbortController();
  const on = (target, name, handler, options = {}) =>
    target.addEventListener(name, handler, {
      ...options,
      signal: controller.signal,
    });
  const listen = (name, handler, options = {}) =>
    on(window, name, handler, options);
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)");
  let lastMotionPreference = reduceMotion.matches;
  const chooseFlow = (key) =>
    window.dispatchEvent(new CustomEvent("sample-flow", { detail: key }));
  if (reduceMotion.matches) {
    $("#rotate-btn").disabled = true;
    $("#rotate-btn").setAttribute("aria-pressed", "false");
    $("#rotate-btn").setAttribute(
      "aria-label",
      "Rotation paused for reduced motion",
    );
    $("#rotate-btn").textContent = "▶";
  }
  let activeScene = 0,
    scrollRatio = 0,
    nearPointer = { x: 0.5, y: 0.5 };
  const shell = $("#cosmos"),
    chapters = $$(".chapter"),
    stage = $(".stage");
  document.documentElement.classList.add("has-js");
  chapters.forEach((e, j) => {
    e.inert = j !== 0;
  });
  function measure() {
    const b = shell.getBoundingClientRect(),
      den = Math.max(1, b.height - innerHeight);
    scrollRatio = Math.min(1, Math.max(0, -b.top / den));
    // A fixed viewport stage remains anchored throughout all 4 chapters. Only opacity changes
    // in the final half-viewport; no scroll-bound vertical translation or reverse bounce.
    const inScene = b.bottom > 0 && b.top < innerHeight;
    stage.inert = !inScene;
    const fade = Math.max(0, Math.min(1, b.bottom / (innerHeight * 0.55)));
    stage.classList.toggle("is-pinned", inScene);
    stage.classList.toggle("is-exiting", fade < 0.2);
    stage.style.setProperty("--stage-opacity", String(fade));
    const ix = Math.min(3, Math.floor((scrollRatio + 0.02) * 4));
    if (ix !== activeScene) {
      activeScene = ix;
      chapters.forEach((e, j) => {
        e.classList.toggle("is-current", j === ix);
        e.inert = j !== ix;
      });
      $("#sceneNo").textContent = String(ix + 1).padStart(2, "0");
      $$("#sceneDots span").forEach((e, j) =>
        e.classList.toggle("on", j === ix),
      );
      stage.dataset.chapter = String(ix);
    }
    let full = document.documentElement.scrollHeight - innerHeight;
    $("#progress").style.width = (full > 0 ? (scrollY / full) * 100 : 0) + "%";
  }
  let measureFrame = 0;
  function scheduleMeasure() {
    if (!measureFrame)
      measureFrame = requestAnimationFrame(() => {
        measureFrame = 0;
        measure();
      });
  }
  listen("scroll", scheduleMeasure, { passive: true });
  listen("resize", scheduleMeasure);
  measure();
  const io = new IntersectionObserver(
    (rows) =>
      rows.forEach((x) => x.target.classList.toggle("in", x.isIntersecting)),
    { threshold: 0.12, rootMargin: "0px 0px -4% 0px" },
  );
  $$(".reveal").forEach((e) => io.observe(e));
  listen(
    "pointermove",
    (e) => {
      nearPointer = { x: e.clientX / innerWidth, y: e.clientY / innerHeight };
      if (!reduceMotion.matches) {
        const glow = $(".cursor-glow");
        glow.style.left = e.clientX + "px";
        glow.style.top = e.clientY + "px";
      }
    },
    { passive: true },
  );
  // Offline 2D canvas globe with true spherical projection, baked coarse global land dots, and reactive markers.
  const canvas = $("#globeCanvas"),
    ctx = canvas.getContext("2d", { alpha: true });
  const points = landPoints.map(([lo, la]) => {
    const a = (lo * Math.PI) / 180,
      b = (la * Math.PI) / 180;
    return {
      x: Math.cos(b) * Math.sin(a),
      y: Math.sin(b),
      z: Math.cos(b) * Math.cos(a),
    };
  });
  const markers = [
    {
      name: "Income",
      desc: "Recognized credits are distinct from other incoming amounts",
      lo: 73,
      la: 19,
      c: "#8bdbc0",
      key: "income",
    },
    {
      name: "Spending",
      desc: "Understand purchases without double counting repayments",
      lo: 112,
      la: 30,
      c: "#eead93",
      key: "spending",
    },
    {
      name: "Transfers",
      desc: "Own-account moves should not inflate consumption",
      lo: 10,
      la: 52,
      c: "#87bbf6",
      key: "transfers",
    },
    {
      name: "Investments",
      desc: "Contributions are tracked separately from spending",
      lo: -49,
      la: -15,
      c: "#bca4ee",
      key: "investments",
    },
    {
      name: "Needs review",
      desc: "Unknown credits should remain open questions",
      lo: -92,
      la: 39,
      c: "#e8cc86",
      key: "review",
    },
  ].map((m) => {
    const a = (m.lo * Math.PI) / 180,
      b = (m.la * Math.PI) / 180;
    return {
      ...m,
      x: Math.cos(b) * Math.sin(a),
      y: Math.sin(b),
      z: Math.cos(b) * Math.cos(a),
      px: 0,
      py: 0,
      visible: false,
    };
  });
  let focusTarget = null;
  let cw = 0,
    ch = 0,
    dpr = 1,
    yaw = 0.98,
    tilt = 0.12,
    zoomScale = 1,
    autoRotate = !reduceMotion.matches,
    vel = 0,
    drag = null,
    hovered = null,
    globeVisible = true,
    lastT = 0,
    drawLoop = 0;
  const M = Math.PI * 2;
  // Location data is only retained in page memory after explicit browser permission.
  // The API's precision is immediately rounded to whole degrees (~110 km grid).
  let approxLocation = null,
    locationMarker = null,
    locationRequest = 0;
  function makeLocationMarker(lat, lon) {
    const a = (lon * Math.PI) / 180,
      b = (lat * Math.PI) / 180;
    return {
      name: "Your approximate area",
      desc: `Approximate only · ${Math.abs(lat)}°${lat < 0 ? "S" : "N"}, ${Math.abs(lon)}°${lon < 0 ? "W" : "E"} · never saved or sent`,
      lo: lon,
      la: lat,
      c: "#fff3bc",
      key: null,
      isUser: true,
      x: Math.cos(b) * Math.sin(a),
      y: Math.sin(b),
      z: Math.cos(b) * Math.cos(a),
      visible: false,
      px: 0,
      py: 0,
    };
  }
  function pauseForLocation() {
    autoRotate = false;
    vel = 0;
    $("#rotate-btn").setAttribute("aria-pressed", "false");
    $("#rotate-btn").setAttribute("aria-label", "Resume globe rotation");
    $("#rotate-btn").title = "Resume globe rotation";
    $("#rotate-btn").textContent = "▶";
  }
  function focusLocation() {
    if (!approxLocation) return;
    pauseForLocation();
    focusTarget = {
      yaw:
        yaw +
        Math.atan2(
          Math.sin((approxLocation.lon * Math.PI) / 180 - yaw),
          Math.cos((approxLocation.lon * Math.PI) / 180 - yaw),
        ),
      tilt: Math.max(
        -1.22,
        Math.min(1.22, (approxLocation.lat * Math.PI) / 180),
      ),
    };
    zoomScale = 1.04;
    $("#globe-status").textContent =
      "Globe focused on your approximate area. Drag to explore.";
  }
  function locationStatus(txt, state) {
    const note = $("#location-note");
    note.textContent = txt;
    note.dataset.state = state || "idle";
  }
  on($("#locate-btn"), "click", () => {
    if (approxLocation) {
      focusLocation();
      return;
    }
    if (!navigator.geolocation || !window.isSecureContext) {
      locationStatus(
        "Location needs a secure browser context (localhost or HTTPS). No location accessed.",
        "error",
      );
      return;
    }
    const request = ++locationRequest;
    const btn = $("#locate-btn");
    $("#clear-location").hidden = false;
    btn.disabled = true;
    btn.textContent = "⌖  Requesting permission…";
    locationStatus(
      "Waiting for your browser permission. Nothing is stored or transmitted by this demo.",
      "pending",
    );
    navigator.geolocation.getCurrentPosition(
      (position) => {
        if (disposed || request !== locationRequest) return;
        if (
          !Number.isFinite(position.coords.latitude) ||
          !Number.isFinite(position.coords.longitude) ||
          Math.abs(position.coords.latitude) > 90 ||
          Math.abs(position.coords.longitude) > 180
        ) {
          btn.disabled = false;
          btn.textContent = "◎ Show my area";
          locationStatus("Location unavailable.", "error");
          return;
        }
        const lat = Math.max(
          -90,
          Math.min(90, Math.round(position.coords.latitude)),
        );
        const lon = Math.max(
          -180,
          Math.min(180, Math.round(position.coords.longitude)),
        );
        approxLocation = { lat, lon };
        locationMarker = makeLocationMarker(lat, lon);
        btn.disabled = false;
        btn.textContent = "◎  Focus on my area";
        $("#clear-location").hidden = false;
        locationStatus(
          `Approximate area: ${Math.abs(lat)}° ${lat < 0 ? "S" : "N"}, ${Math.abs(lon)}° ${lon < 0 ? "W" : "E"}. Shown on this globe only.`,
          "shown",
        );
        focusLocation();
      },
      (error) => {
        if (disposed || request !== locationRequest) return;
        btn.disabled = false;
        btn.textContent = "◎  Show my area";
        locationStatus(
          error.code === 1
            ? "Permission declined. The globe works without location."
            : error.code === 3
              ? "Location timed out. Try again if you wish."
              : "Location unavailable. The globe works without it.",
          "error",
        );
      },
      { enableHighAccuracy: false, timeout: 9000, maximumAge: 0 },
    );
  });
  on($("#clear-location"), "click", () => {
    locationRequest++;
    $("#locate-btn").disabled = false;
    hovered = null;
    hideTip();
    approxLocation = null;
    locationMarker = null;
    focusTarget = null;
    $("#clear-location").hidden = true;
    $("#locate-btn").textContent = "◎  Show my area";
    locationStatus(
      "Location cleared from this page. No location is saved or sent.",
      "idle",
    );
    $("#globe-status").textContent = "Approximate location marker removed.";
  });
  function resize() {
    const rect = canvas.getBoundingClientRect();
    cw = rect.width;
    ch = rect.height;
    dpr = Math.min(devicePixelRatio || 1, 1.75);
    canvas.width = Math.round(cw * dpr);
    canvas.height = Math.round(ch * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  resize();
  listen("resize", resize);
  const visibilityObs = new IntersectionObserver(
    (rows) => {
      globeVisible = rows[0].isIntersecting;
    },
    { threshold: 0 },
  );
  visibilityObs.observe(canvas);
  function coords(p, az, at) {
    const s = Math.sin(az),
      c = Math.cos(az);
    const xx = p.x * c - p.z * s,
      zz = p.z * c + p.x * s;
    const ca = Math.cos(at),
      sa = Math.sin(at);
    return [xx, p.y * ca - zz * sa, zz * ca + p.y * sa];
  }
  function globeGeom() {
    const mobile = cw < 700;
    let r = Math.min(
      ch * (mobile ? 0.285 : 0.435),
      cw * (mobile ? 0.52 : 0.315),
    );
    return {
      cx: cw * (mobile ? 0.55 : 0.71),
      cy: ch * (mobile ? 0.72 : 0.52),
      r: r * zoomScale,
    };
  }
  function draw(t) {
    // Also synchronize when a browser updates matches before dispatching change.
    if (lastMotionPreference !== reduceMotion.matches) syncMotionPreference();
    drawLoop = requestAnimationFrame(draw);
    if (document.hidden || !globeVisible || !cw || !ch) return;
    if (reduceMotion.matches) t = 0;
    const dt = Math.min(0.06, Math.max(0, (t - lastT) / 1000 || 0.016));
    lastT = t;
    if (focusTarget) {
      const a = reduceMotion.matches ? 1 : Math.min(1, dt * 8);
      yaw += (focusTarget.yaw - yaw) * a;
      tilt += (focusTarget.tilt - tilt) * a;
      if (
        Math.abs(yaw - focusTarget.yaw) + Math.abs(tilt - focusTarget.tilt) <
        0.001
      )
        focusTarget = null;
    }
    if (!drag && !reduceMotion.matches) {
      yaw += ((autoRotate ? 0.07 : 0) + vel) * dt;
      vel *= Math.pow(0.92, dt * 60);
    }
    // Scroll transitions change the story, not the globe's position or rotation direction.
    let az = yaw + (reduceMotion.matches ? 0 : (nearPointer.x - 0.5) * 0.025),
      at = tilt + (reduceMotion.matches ? 0 : (nearPointer.y - 0.5) * 0.018);
    const { cx, cy, r } = globeGeom();
    ctx.clearRect(0, 0, cw, ch);
    // Background stars, subdued for legibility.
    for (let k = 0; k < 100; k++) {
      let x = (Math.sin(k * 53.131) * 0.5 + 0.5) * cw,
        y = (Math.sin(k * 91.721) * 0.5 + 0.5) * ch;
      ctx.fillStyle = `rgba(181,246,231,${0.055 + (0.04 * (1 + Math.sin(t * 0.00065 + k))) / 2})`;
      ctx.fillRect(x, y, 1, 1);
    }
    const halo = ctx.createRadialGradient(cx, cy, r * 0.4, cx, cy, r * 1.48);
    halo.addColorStop(0, "rgba(76,190,178,0)");
    halo.addColorStop(0.68, "rgba(59,159,160,.025)");
    halo.addColorStop(0.85, "rgba(79,223,203,.105)");
    halo.addColorStop(1, "rgba(11,75,75,0)");
    ctx.fillStyle = halo;
    ctx.beginPath();
    ctx.arc(cx, cy, r * 1.5, 0, M);
    ctx.fill();
    const ocean = ctx.createRadialGradient(
      cx - r * 0.4,
      cy - r * 0.48,
      0,
      cx,
      cy,
      r * 1.24,
    );
    ocean.addColorStop(0, "#1b5964");
    ocean.addColorStop(0.48, "#123744");
    ocean.addColorStop(0.82, "#071f2d");
    ocean.addColorStop(1, "#030f18");
    ctx.fillStyle = ocean;
    ctx.beginPath();
    ctx.arc(cx, cy, r, 0, M);
    ctx.fill();
    ctx.save();
    ctx.beginPath();
    ctx.arc(cx, cy, r, 0, M);
    ctx.clip();
    ctx.lineWidth = 0.65;
    // Latitude rings and curved meridians, back-face removed by spherical coordinates.
    for (let lat = -70; lat <= 70; lat += 20) {
      ctx.beginPath();
      let began = false;
      for (let lon = -180; lon <= 180; lon += 3) {
        let a = (lon * Math.PI) / 180,
          b = (lat * Math.PI) / 180;
        const p = coords(
          {
            x: Math.cos(b) * Math.sin(a),
            y: Math.sin(b),
            z: Math.cos(b) * Math.cos(a),
          },
          az,
          at,
        );
        if (p[2] > 0.02) {
          const x = cx + p[0] * r,
            y = cy - p[1] * r;
          if (!began) {
            ctx.moveTo(x, y);
            began = true;
          } else ctx.lineTo(x, y);
        } else began = false;
      }
      ctx.strokeStyle = "rgba(129,198,197,.09)";
      ctx.stroke();
    }
    for (let lon = -180; lon < 180; lon += 20) {
      ctx.beginPath();
      let began = false;
      for (let lat = -87; lat <= 87; lat += 3) {
        let a = (lon * Math.PI) / 180,
          b = (lat * Math.PI) / 180;
        const p = coords(
          {
            x: Math.cos(b) * Math.sin(a),
            y: Math.sin(b),
            z: Math.cos(b) * Math.cos(a),
          },
          az,
          at,
        );
        if (p[2] > 0.02) {
          let x = cx + p[0] * r,
            y = cy - p[1] * r;
          if (!began) {
            ctx.moveTo(x, y);
            began = true;
          } else ctx.lineTo(x, y);
        } else began = false;
      }
      ctx.strokeStyle = "rgba(129,198,197,.075)";
      ctx.stroke();
    }
    for (let i = 0; i < points.length; i++) {
      let p = coords(points[i], az, at);
      if (p[2] <= 0) continue;
      let a = 0.23 + 0.72 * Math.pow(p[2], 0.45);
      let sz = r * 0.0038 * (0.7 + 0.7 * p[2]);
      ctx.fillStyle = `rgba(171,235,199,${a})`;
      ctx.beginPath();
      ctx.arc(cx + p[0] * r, cy - p[1] * r, sz, 0, M);
      ctx.fill();
    }
    ctx.restore();
    ctx.strokeStyle = "rgba(160,251,223,.39)";
    ctx.lineWidth = 1.1;
    ctx.beginPath();
    ctx.arc(cx, cy, r, 0, M);
    ctx.stroke();
    // Fine concentric orbital bands.
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(-0.25);
    ctx.strokeStyle = "rgba(118,212,208,.18)";
    ctx.lineWidth = 0.85;
    ctx.beginPath();
    ctx.ellipse(0, 0, r * 1.15, r * 0.37, 0, 0, M);
    ctx.stroke();
    ctx.beginPath();
    ctx.ellipse(0, 0, r * 1.29, r * 0.47, 0, 0.34, Math.PI * 1.32);
    ctx.stroke();
    ctx.restore();
    // Great-circle-like visual links between projected front-facing markers.
    const ps = [...markers, ...(locationMarker ? [locationMarker] : [])].map(
      (m) => {
        let p = coords(m, az, at);
        m.visible = p[2] > 0.03;
        m.px = cx + p[0] * r;
        m.py = cy - p[1] * r;
        m.depth = p[2];
        return m;
      },
    );
    let visible = ps.filter((m) => m.visible);
    if (visible.length > 1) {
      const base = visible[0];
      for (let j = 1; j < visible.length; j++) {
        let end = visible[j];
        ctx.beginPath();
        ctx.moveTo(base.px, base.py);
        let h = Math.min(
          75,
          Math.hypot(end.px - base.px, end.py - base.py) * 0.3,
        );
        ctx.quadraticCurveTo(
          (base.px + end.px) / 2,
          (base.py + end.py) / 2 - h,
          end.px,
          end.py,
        );
        ctx.strokeStyle = `rgba(147,230,214,${0.13 + 0.08 * Math.sin(t * 0.001 + j)})`;
        ctx.lineWidth = 1.2;
        ctx.stroke();
      }
    }
    for (let m of visible) {
      let rad = m.isUser ? 7 : hovered === m ? 6.8 : 4.5;
      ctx.beginPath();
      ctx.fillStyle = m.c + "21";
      ctx.arc(m.px, m.py, rad * 3, 0, M);
      ctx.fill();
      ctx.beginPath();
      ctx.fillStyle = m.c;
      ctx.arc(m.px, m.py, rad, 0, M);
      ctx.fill();
      ctx.strokeStyle = "#e7ffef";
      ctx.lineWidth = m.isUser ? 1.8 : 1;
      ctx.stroke();
      if (hovered === m || m.isUser) {
        ctx.beginPath();
        ctx.strokeStyle = m.c;
        ctx.lineWidth = m.isUser ? 1.7 : 1;
        ctx.arc(
          m.px,
          m.py,
          12 + (reduceMotion.matches ? 0 : Math.sin(t * 0.003) * 2),
          0,
          M,
        );
        ctx.stroke();
      }
      if (m.isUser) {
        ctx.save();
        ctx.font = "700 11px Inter,system-ui,sans-serif";
        ctx.textAlign = "left";
        ctx.strokeStyle = "#0b2730";
        ctx.lineWidth = 4;
        ctx.strokeText("YOUR AREA · APPROX.", m.px + 17, m.py - 11);
        ctx.fillStyle = "#fff3bc";
        ctx.fillText("YOUR AREA · APPROX.", m.px + 17, m.py - 11);
        ctx.restore();
      }
    }
  }
  drawLoop = requestAnimationFrame(draw);
  function globeLocal(e) {
    let b = canvas.getBoundingClientRect();
    return { x: e.clientX - b.left, y: e.clientY - b.top };
  }
  function hit(e) {
    let { x, y } = globeLocal(e);
    let h = null,
      d = 18;
    for (let m of [...markers, ...(locationMarker ? [locationMarker] : [])]) {
      if (!m.visible) continue;
      let n = Math.hypot(x - m.px, y - m.py);
      if (n < d) {
        h = m;
        d = n;
      }
    }
    return h;
  }
  function hideTip() {
    $("#globeTip").classList.remove("show");
    $("#globeTip").setAttribute("aria-hidden", "true");
  }
  on(canvas, "pointerdown", (e) => {
    if (drag || (e.pointerType === "mouse" && e.button !== 0)) return;
    let p = globeLocal(e);
    focusTarget = null;
    drag = {
      id: e.pointerId,
      x: p.x,
      y: p.y,
      last: p.x,
      lastY: p.y,
      dragged: false,
      time: performance.now(),
    };
    canvas.setPointerCapture(e.pointerId);
    canvas.classList.add("grabbing");
    hideTip();
  });
  on(canvas, "pointermove", (e) => {
    if (drag) {
      if (e.pointerId !== drag.id) return;
      let p = globeLocal(e),
        dx = p.x - drag.last,
        dy = p.y - drag.lastY;
      drag.lastY = p.y;
      drag.last = p.x;
      drag.dragged ||= Math.abs(p.x - drag.x) + Math.abs(p.y - drag.y) > 7;
      yaw -= dx * 0.0048;
      vel = Math.max(-1.8, Math.min(1.8, -dx * 0.14));
      tilt = Math.max(-1.22, Math.min(1.22, tilt - dy * 0.003));
      return;
    }
    hovered = hit(e);
    if (hovered) {
      let p = globeLocal(e);
      const tip = $("#globeTip");
      tip.querySelector("strong").textContent = hovered.name;
      tip.querySelector("strong").style.color = hovered.c;
      tip.querySelector("small").textContent = hovered.desc;
      tip.style.left = Math.min(cw - 232, Math.max(8, p.x + 18)) + "px";
      tip.style.top = Math.min(ch - 105, Math.max(8, p.y - 80)) + "px";
      tip.classList.add("show");
      tip.setAttribute("aria-hidden", "false");
      canvas.style.cursor = "pointer";
    } else {
      hideTip();
      canvas.style.cursor = "grab";
    }
  });
  function release(e) {
    if (!drag || e.pointerId !== drag.id) return;
    const wasDragging = drag.dragged;
    drag = null;
    canvas.classList.remove("grabbing");
    if (!wasDragging) {
      let h = hit(e);
      if (h) {
        if (h.isUser) {
          $("#globe-status").textContent =
            "Your approximate area marker. No exact location is stored or shared.";
        } else {
          chooseFlow(h.key);
          document.getElementById("flow")?.scrollIntoView({
            behavior: reduceMotion.matches ? "auto" : "smooth",
            block: "start",
          });
          $("#globe-status").textContent =
            `Selected ${h.name}. Details are in the Money flows section.`;
        }
      }
    }
  }
  on(canvas, "pointerup", release);
  on(canvas, "pointercancel", () => {
    drag = null;
    canvas.classList.remove("grabbing");
  });
  on(canvas, "pointerleave", () => {
    hovered = null;
    hideTip();
  });
  on(canvas, "keydown", (e) => {
    if (e.key === "ArrowLeft" || e.key === "ArrowRight") {
      e.preventDefault();
      yaw += e.key === "ArrowLeft" ? -0.2 : 0.2;
      $("#globe-status").textContent = "Globe rotated using keyboard.";
    }
    if (e.key === "Home") {
      e.preventDefault();
      yaw = 0.98;
      tilt = 0.12;
      zoomScale = 1;
    }
    if (e.key === "+" || e.key === "=") {
      e.preventDefault();
      zoomScale = Math.min(1.24, zoomScale + 0.12);
    }
    if (e.key === "-") {
      e.preventDefault();
      zoomScale = Math.max(0.72, zoomScale - 0.12);
    }
  });
  on($("#rotate-btn"), "click", () => {
    autoRotate = reduceMotion.matches ? false : !autoRotate;
    vel = 0;
    $("#rotate-btn").setAttribute("aria-pressed", String(autoRotate));
    $("#rotate-btn").setAttribute(
      "aria-label",
      autoRotate ? "Pause globe rotation" : "Resume globe rotation",
    );
    $("#rotate-btn").title = autoRotate
      ? "Pause globe rotation"
      : "Resume globe rotation";
    $("#rotate-btn").textContent = autoRotate ? "Ⅱ" : "▶";
    $("#globe-status").textContent = autoRotate
      ? "Globe rotation resumed."
      : "Globe rotation paused.";
  });
  on($("#zoom-in"), "click", () => {
    zoomScale = Math.min(1.24, zoomScale + 0.12);
    $("#globe-status").textContent = "Globe zoomed in.";
  });
  on($("#zoom-out"), "click", () => {
    zoomScale = Math.max(0.72, zoomScale - 0.12);
    $("#globe-status").textContent = "Globe zoomed out.";
  });
  on($("#reset-btn"), "click", () => {
    focusTarget = null;
    yaw = 0.98;
    tilt = 0.12;
    zoomScale = 1;
    vel = 0;
    $("#globe-status").textContent = "Globe reset to original view.";
  });
  function syncMotionPreference() {
    lastMotionPreference = reduceMotion.matches;
    const button = $("#rotate-btn");
    button.disabled = reduceMotion.matches;
    autoRotate = false;
    vel = 0;
    button.setAttribute("aria-pressed", "false");
    button.textContent = "▶";
    const label = reduceMotion.matches
      ? "Automatic rotation disabled by reduced motion"
      : "Resume globe rotation";
    button.setAttribute("aria-label", label);
    button.title = label;
  }
  on(reduceMotion, "change", syncMotionPreference);

  return () => {
    disposed = true;
    locationRequest++;
    controller.abort();
    cancelAnimationFrame(drawLoop);
    cancelAnimationFrame(measureFrame);
    io.disconnect();
    visibilityObs.disconnect();
    approxLocation = null;
    locationMarker = null;
    hovered = null;
    document.documentElement.classList.remove("has-js");
  };
}
