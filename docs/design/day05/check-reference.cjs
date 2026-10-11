// Design-reference checks only. No production app, dependencies or genuine location.
// Usage: node check-reference.cjs [absolute path to an existing playwright package]
const { chromium } = require(process.argv[2] || 'playwright');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const assert = require('node:assert/strict');
const root = __dirname;
const evidence = path.join(root, 'evidence');
const html = fs.readFileSync(path.join(root, 'reference/FINNest_Interactive_Globe_V4.html'));
const results = [];
const errors = [];
const network = [];
let browser;
const server = http.createServer((req, res) => {
  if (req.url !== '/' && req.url !== '/favicon.ico') { res.writeHead(404); res.end(); return; }
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.end(req.url === '/' ? html : '');
});
async function check(name, run) {
  try { results.push({ name, status: 'pass', detail: await run() }); }
  catch (error) { results.push({ name, status: 'fail', detail: error.message.slice(0, 1500) }); }
}
async function pageFor(viewport, mode = 'grant', reducedMotion = 'no-preference', touch = false) {
  const context = await browser.newContext({ viewport, reducedMotion, hasTouch: touch });
  await context.addInitScript(({ mode }) => {
    window.__geoCalls = 0;
    // Synthetic callback only; the browser/OS geolocation provider is never called.
    Object.defineProperty(navigator, 'geolocation', { configurable: true, value: mode === 'missing' ? undefined : {
      getCurrentPosition(success, failure) {
        window.__geoCalls++;
        setTimeout(() => mode === 'grant'
          ? success({ coords: { latitude: 25.4358, longitude: 81.8463 } })
          : failure({ code: mode === 'deny' ? 1 : mode === 'timeout' ? 3 : 2 }), 0);
      }
    }});
    if (mode === 'insecure') Object.defineProperty(window, 'isSecureContext', { value: false });
    // Observe draw calls without changing the reference renderer or financial logic.
    window.__circles = [];
    const clear = CanvasRenderingContext2D.prototype.clearRect;
    const arc = CanvasRenderingContext2D.prototype.arc;
    CanvasRenderingContext2D.prototype.clearRect = function (...args) { window.__circles = []; return clear.apply(this, args); };
    CanvasRenderingContext2D.prototype.arc = function (x, y, r, ...args) {
      window.__circles.push({ x, y, r }); return arc.call(this, x, y, r, ...args);
    };
  }, { mode });
  const page = await context.newPage();
  page.on('pageerror', error => errors.push(error.message));
  page.on('request', req => { if (!req.url().startsWith(base)) network.push(req.url()); });
  await page.goto(base);
  await page.waitForTimeout(150);
  return page;
}
const markers = page => page.evaluate(() => window.__circles.filter(c => c.r === 4.5));
let base;
(async () => {
  fs.mkdirSync(evidence, { recursive: true });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  base = `http://127.0.0.1:${server.address().port}/`;
  browser = await chromium.launch({ headless: true, channel: process.env.DESIGN_BROWSER_CHANNEL || 'chrome' });
  const desktop = await pageFor({ width: 1440, height: 900 });
  await check('No automatic location request', async () => assert.equal(await desktop.evaluate(() => window.__geoCalls), 0));
  await desktop.screenshot({ path: path.join(evidence, 'desktop-hero.png') });
  await check('Automatic rotation changes marker projection', async () => {
    const before = await markers(desktop); await desktop.waitForTimeout(250);
    assert.notDeepEqual(await markers(desktop), before);
  });
  await desktop.locator('#rotate-btn').click();
  await check('Pause stops marker rotation', async () => {
    await desktop.waitForTimeout(100); const before = await markers(desktop);
    await desktop.waitForTimeout(150); assert.deepEqual(await markers(desktop), before);
    assert.equal(await desktop.locator('#rotate-btn').getAttribute('aria-pressed'), 'false');
  });
  await check('Marker hover exposes explanatory tooltip', async () => {
    const [m] = await markers(desktop); assert.ok(m);
    await desktop.mouse.move(m.x, m.y); await desktop.waitForTimeout(60);
    assert.equal(await desktop.locator('#globeTip').getAttribute('aria-hidden'), 'false');
    assert.ok(await desktop.locator('#globeTip strong').textContent());
  });
  await check('Desktop dragging changes globe projection', async () => {
    await desktop.mouse.move(1080, 580); await desktop.waitForTimeout(60);
    const before = await markers(desktop);
    await desktop.mouse.down(); await desktop.mouse.move(1200, 580, { steps: 12 }); await desktop.mouse.up();
    await desktop.waitForTimeout(100); assert.notDeepEqual(await markers(desktop), before);
  });
  await desktop.locator('#reset-btn').click();
  await check('Zoom changes rendered globe radius; reset restores it', async () => {
    const radius = () => desktop.evaluate(() => Math.max(...window.__circles.map(c => c.r)));
    await desktop.waitForTimeout(60); const original = await radius();
    await desktop.locator('#zoom-in').click(); await desktop.waitForTimeout(60); assert.ok(await radius() > original);
    await desktop.locator('#zoom-out').click(); await desktop.waitForTimeout(60); assert.ok(Math.abs(await radius() - original) < 0.1);
    await desktop.locator('#reset-btn').click(); await desktop.waitForTimeout(60); assert.ok(Math.abs(await radius() - original) < 0.1);
  });
  await check('Four chapters keep canvas anchored; stage fades at exit', async () => {
    const samples = [];
    for (const [y, label] of [[0,'01'],[750,'02'],[1450,'03'],[2200,'04'],[2750,'04']]) {
      await desktop.evaluate(y => window.scrollTo({ top: y, behavior: 'instant' }), y); await desktop.waitForTimeout(80);
      const box = await desktop.locator('#globeCanvas').boundingBox();
      assert.equal(box.y, 0); assert.equal(await desktop.locator('#sceneNo').textContent(), label);
      samples.push({ scrollY: y, canvasY: box.y, chapter: label });
    }
    await desktop.evaluate(() => window.scrollTo({ top: document.querySelector('#cosmos').offsetHeight - 150, behavior: 'instant' }));
    await desktop.waitForTimeout(80);
    const opacity = await desktop.locator('.stage').evaluate(e => Number(getComputedStyle(e).opacity));
    assert.ok(opacity > 0 && opacity < 1); return { samples, exitOpacity: opacity };
  });
  await check('Scrolling forward and backward does not rotate paused globe', async () => {
    const before = await markers(desktop);
    for (const y of [1000, 2000, 1000]) { await desktop.evaluate(y => window.scrollTo({ top: y, behavior: 'instant' }), y); await desktop.waitForTimeout(50); }
    assert.deepEqual(await markers(desktop), before);
  });
  await check('All five financial categories select corresponding path', async () => {
    for (const category of ['income','spending','transfers','investments','review']) {
      const button = desktop.locator(`[data-category="${category}"]`); await button.click();
      assert.equal(await button.getAttribute('aria-pressed'), 'true');
      assert.equal(await desktop.locator('.flow-line.sel').getAttribute('data-flow'), category);
    }
  });
  await check('Fictional credit classifications match declared totals and undo', async () => {
    for (const [key, income, transfer, unknown] of [['income','₹85,600','₹15,000','₹0'],['transfer','₹82,000','₹18,600','₹0'],['unknown','₹82,000','₹15,000','₹3,600']]) {
      await desktop.locator(`[data-classification="${key}"]`).click();
      assert.equal(await desktop.locator('#income-total').textContent(), income);
      assert.equal(await desktop.locator('#transfer-total').textContent(), transfer);
      assert.equal(await desktop.locator('#unknown-total').textContent(), unknown);
      assert.ok((await desktop.locator('.metric-grid').innerText()).includes('₹30,750'));
    }
  });
  await desktop.locator('#mockapp').screenshot({ path: path.join(evidence, 'desktop-dashboard.png') });
  await desktop.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
  await desktop.waitForTimeout(100);
  await check('Mock location grant rounds display; clear removes marker', async () => {
    await desktop.locator('#locate-btn').click();
    await desktop.locator('#location-note[data-state="shown"]').waitFor();
    assert.match(await desktop.locator('#location-note').textContent(), /25° N, 82° E/);
    assert.equal(await desktop.locator('#rotate-btn').getAttribute('aria-pressed'), 'false');
    await desktop.screenshot({ path: path.join(evidence, 'desktop-location-mock.png') });
    await desktop.locator('#reset-btn').click();
    assert.equal(await desktop.locator('#clear-location').isVisible(), true); // reset is orientation only
    await desktop.locator('#clear-location').click();
    assert.equal(await desktop.locator('#clear-location').isVisible(), false);
    await desktop.waitForTimeout(50);
    assert.equal(await desktop.evaluate(() => window.__circles.some(c => c.r === 7)), false);
    assert.equal(await desktop.evaluate(() => localStorage.length + sessionStorage.length), 0);
  });
  for (const [mode, message] of [['deny','Permission declined'],['timeout','Location timed out'],['unavailable','Location unavailable'],['missing','secure browser context'],['insecure','secure browser context']]) {
    await check(`Mock location ${mode}`, async () => {
      const page = await pageFor({ width:1440, height:900 }, mode);
      await page.locator('#locate-btn').click(); await page.waitForTimeout(60);
      assert.ok((await page.locator('#location-note').textContent()).includes(message));
      if (['missing','insecure'].includes(mode)) assert.equal(await page.evaluate(() => window.__geoCalls), 0);
      await page.context().close();
    });
  }
  const mobile = await pageFor({ width:390, height:844 }, 'grant', 'no-preference', true);
  await mobile.screenshot({ path:path.join(evidence,'mobile-hero.png') });
  await check('Mobile location control clickable without forced click', async () => {
    await mobile.locator('#locate-btn').click(); await mobile.locator('#location-note[data-state="shown"]').waitFor();
    await mobile.screenshot({ path:path.join(evidence,'mobile-location-mock.png') });
    await mobile.locator('#clear-location').click();
  });
  await check('Mobile menu toggles and demo CTA navigates', async () => {
    await mobile.locator('#menu').click(); assert.equal(await mobile.locator('#menu').getAttribute('aria-expanded'), 'true');
    await mobile.locator('#navlinks a[href="#demo"]').click(); await mobile.waitForTimeout(1000);
    assert.equal(await mobile.locator('#menu').getAttribute('aria-expanded'), 'false'); assert.equal(new URL(mobile.url()).hash, '#demo');
  });
  await check('Touch pointer drag changes projection (synthetic events)', async () => {
    await mobile.evaluate(() => window.scrollTo({top:0,behavior:'instant'})); await mobile.waitForTimeout(80);
    if (await mobile.locator('#rotate-btn').getAttribute('aria-pressed') === 'true') await mobile.locator('#rotate-btn').click();
    await mobile.waitForTimeout(80); const before=await markers(mobile);
    const cdp=await mobile.context().newCDPSession(mobile);
    await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:80,y:570}]});
    await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:150,y:570}]});
    await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
    await mobile.waitForTimeout(80); assert.notDeepEqual(await markers(mobile),before);
  });
  for (const [width,height] of [[1440,900],[768,1024],[390,844],[320,568]]) await check(`No horizontal overflow ${width}x${height}`,async()=>{
    const page=await pageFor({width,height});
    const measured=await page.evaluate(()=>({width:innerWidth,scrollWidth:document.documentElement.scrollWidth}));
    assert.ok(measured.scrollWidth<=measured.width,JSON.stringify(measured)); await page.context().close(); return measured;
  });
  await check('Compact mobile transaction rows fit their container',async()=>{
    const page=await pageFor({width:320,height:568});
    await page.locator('#mockapp').scrollIntoViewIfNeeded(); await page.waitForTimeout(150);
    await page.locator('#mockapp').screenshot({path:path.join(evidence,'compact-mobile-dashboard.png')});
    const clipped=await page.locator('.tx-row').evaluateAll(rows=>rows.map(e=>({width:e.clientWidth,scrollWidth:e.scrollWidth})).filter(e=>e.scrollWidth>e.width));
    assert.deepEqual(clipped,[],'Transaction cells overflow their row'); await page.context().close();
  });
  await check('Keyboard focus and globe arrow controls',async()=>{
    await desktop.locator('#globeCanvas').focus();
    const before=await markers(desktop); await desktop.keyboard.press('ArrowRight'); await desktop.waitForTimeout(80);
    assert.notDeepEqual(await markers(desktop),before);
    const outline=await desktop.locator('#globeCanvas').evaluate(e=>getComputedStyle(e).outlineStyle);
    assert.notEqual(outline,'none');
  });
  await check('Reduced motion disables initial automatic rotation',async()=>{
    const page=await pageFor({width:1440,height:900},'grant','reduce');
    assert.equal(await page.locator('#rotate-btn').getAttribute('aria-pressed'),'false');
    const before=await markers(page); await page.waitForTimeout(100); assert.deepEqual(await markers(page),before);
    await page.context().close();
  });
  await check('Reduced motion removes all decorative canvas animation',async()=>{
    const page=await pageFor({width:1440,height:900},'grant','reduce');
    const pixels=()=>page.locator('#globeCanvas').evaluate(c=>c.toDataURL());
    const before=await pixels(); await page.waitForTimeout(180); assert.ok((await pixels())===before,'Canvas pixels still change with reduced motion');
    await page.context().close();
  });
  await check('No page errors or third-party requests',async()=>{assert.deepEqual(errors,[]); assert.deepEqual(network,[]);});
})().catch(error=>results.push({name:'Harness execution',status:'blocked',detail:error.message})).finally(async()=>{
  if(browser)await browser.close(); server.close();
  fs.mkdirSync(evidence,{recursive:true});
  const report={date:new Date().toISOString(),target:'Unmodified founder reference, not an implemented frontend',browser:`Installed ${process.env.DESIGN_BROWSER_CHANNEL || 'chrome'} headless via Playwright`,location:'Mock callbacks only; no genuine location accessed',results};
  fs.writeFileSync(path.join(evidence,'reference-checks.json'),JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(results.map(({name,status,detail})=>({name,status,detail:typeof detail==='string'?detail.slice(0,350):detail})),null,2));
  process.exitCode=results.some(r=>r.status!=='pass')?1:0;
});
