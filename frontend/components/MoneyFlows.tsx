"use client";
import { useState, useEffect, type CSSProperties } from "react";
import { flowMeta, type FlowKey } from "../lib/flow";
export function MoneyFlows({ brand }: { brand: string }) {
  const [selected, setSelected] = useState<FlowKey>("income");
  useEffect(() => {
    const choose = (event: Event) => {
      const key = (event as CustomEvent<string>).detail;
      if (key in flowMeta) setSelected(key as FlowKey);
    };
    window.addEventListener("sample-flow", choose);
    return () => window.removeEventListener("sample-flow", choose);
  }, []);
  const meta = flowMeta[selected];
  const count =
    String(Object.keys(flowMeta).indexOf(selected) + 1).padStart(2, "0") +
    " / 05";
  const label =
    count.slice(0, 2) +
    " / " +
    (selected === "review" ? "NEEDS REVIEW" : selected.toUpperCase());
  return (
    <section id="flow" className="section">
      <div className="flow-head reveal">
        <div>
          <div className="overline">Move the cursor. Discover the meaning.</div>
          <h2>
            Every rupee has
            <br />
            <em>its own route.</em>
          </h2>
        </div>
        <p className="lede">
          Select a category to follow a different money path. The color has
          meaning—and the meaning changes the report.
        </p>
      </div>
      <div className="flow-grid">
        <div className="flow-map reveal">
          <svg
            className="flow-svg"
            viewBox="0 0 480 450"
            role="img"
            aria-label={`Five routes from the ${brand} center representing income, spending, transfers, investments and needs review`}
          >
            <defs>
              <filter id="sg">
                <feGaussianBlur stdDeviation="4"></feGaussianBlur>
              </filter>
            </defs>
            <path className="path-bg" d="M238 220 C130 192 104 98 62 55"></path>
            <path
              className="path-bg"
              d="M239 220 C337 140 385 125 425 79"
            ></path>
            <path
              className="path-bg"
              d="M242 225 C350 233 398 288 429 364"
            ></path>
            <path
              className="path-bg"
              d="M238 224 C157 310 129 342 64 391"
            ></path>
            <path
              className="path-bg"
              d="M242 222 C225 118 240 91 255 29"
            ></path>
            <path
              className={selected === "income" ? "flow-line sel" : "flow-line"}
              data-flow="income"
              style={{ stroke: "var(--mint)" } as CSSProperties}
              d="M238 220 C130 192 104 98 62 55"
            ></path>
            <path
              className={
                selected === "spending" ? "flow-line sel" : "flow-line"
              }
              data-flow="spending"
              style={{ stroke: "var(--coral)" } as CSSProperties}
              d="M239 220 C337 140 385 125 425 79"
            ></path>
            <path
              className={
                selected === "transfers" ? "flow-line sel" : "flow-line"
              }
              data-flow="transfers"
              style={{ stroke: "var(--blue)" } as CSSProperties}
              d="M242 225 C350 233 398 288 429 364"
            ></path>
            <path
              className={
                selected === "investments" ? "flow-line sel" : "flow-line"
              }
              data-flow="investments"
              style={{ stroke: "var(--violet)" } as CSSProperties}
              d="M238 224 C157 310 129 342 64 391"
            ></path>
            <path
              className={selected === "review" ? "flow-line sel" : "flow-line"}
              data-flow="review"
              style={{ stroke: "var(--gold)" } as CSSProperties}
              d="M242 222 C225 118 240 91 255 29"
            ></path>
            <circle cx="61" cy="55" r="15" fill="#8eddb7"></circle>
            <circle cx="425" cy="79" r="15" fill="#e7a78d"></circle>
            <circle cx="429" cy="364" r="15" fill="#87bbf6"></circle>
            <circle cx="64" cy="391" r="15" fill="#bca4ee"></circle>
            <circle cx="255" cy="29" r="15" fill="#ddc77e"></circle>
            <g
              fill="#1a4745"
              fontSize="10"
              fontFamily="monospace"
              textAnchor="middle"
            >
              <text x="61" y="59">
                +
              </text>
              <text x="425" y="83">
                −
              </text>
              <text x="429" y="368">
                ↔
              </text>
              <text x="64" y="395">
                ↗
              </text>
              <text x="255" y="33">
                ?
              </text>
            </g>
          </svg>
          <div className="map-center">
            <small>EVERY ROUTE</small>
            <strong>{brand}</strong>
          </div>
          <div className="map-hint">
            ILLUSTRATIVE FINANCIAL ROUTES · NOT A LIVE DATA CONNECTION
          </div>
        </div>
        <div className="flow-detail reveal">
          <div>
            <div
              className="flow-category"
              id="flow-label"
              style={{ color: meta.color }}
            >
              {label}
            </div>
            <h3 id="flow-heading">{meta.heading}</h3>
            <p id="flow-copy" className="flow-explain">
              {meta.copy}
            </p>
            <div
              className="flow-filters"
              role="group"
              aria-label="Explore financial flow categories"
            >
              <button
                className="flow-filter"
                data-category="income"
                aria-pressed={selected === "income"}
                onClick={() => setSelected("income")}
                style={{ "--swatch": "var(--mint)" } as CSSProperties}
              >
                <i></i>Income
              </button>
              <button
                className="flow-filter"
                data-category="spending"
                aria-pressed={selected === "spending"}
                onClick={() => setSelected("spending")}
                style={{ "--swatch": "var(--coral)" } as CSSProperties}
              >
                <i></i>Spending
              </button>
              <button
                className="flow-filter"
                data-category="transfers"
                aria-pressed={selected === "transfers"}
                onClick={() => setSelected("transfers")}
                style={{ "--swatch": "var(--blue)" } as CSSProperties}
              >
                <i></i>Transfers
              </button>
              <button
                className="flow-filter"
                data-category="investments"
                aria-pressed={selected === "investments"}
                onClick={() => setSelected("investments")}
                style={{ "--swatch": "var(--violet)" } as CSSProperties}
              >
                <i></i>Investments
              </button>
              <button
                className="flow-filter"
                data-category="review"
                aria-pressed={selected === "review"}
                onClick={() => setSelected("review")}
                style={{ "--swatch": "var(--gold)" } as CSSProperties}
              >
                <i></i>Needs review
              </button>
            </div>
          </div>
          <div className="flow-foot">
            <span>INTERACTIVE CONCEPT · NO BANK CONNECTION</span>
            <span id="flow-count">{count}</span>
          </div>
        </div>
      </div>
    </section>
  );
}
