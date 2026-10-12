"use client";
import { useEffect, useRef, type CSSProperties } from "react";
import { initializeGlobe } from "../lib/globe-runtime";
export function GlobeStory({ brand }: { brand: string }) {
  const root = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (root.current) return initializeGlobe(root.current);
  }, []);
  return (
    <div ref={root}>
      <div id="progress" aria-hidden="true" />
      <div className="cursor-glow" aria-hidden="true" />
      <section
        className="scene-shell"
        id="cosmos"
        aria-label="Interactive money world introduction"
      >
        <div className="stage">
          <div className="globe-atmosphere" aria-hidden="true"></div>
          <canvas
            id="globeCanvas"
            tabIndex={0}
            role="img"
            aria-label="Interactive revolving globe representing financial flows. Drag to rotate. Use left and right arrow keys when focused. Select a financial category in the Money flows section below for the same information."
            aria-describedby="globe-status"
          ></canvas>
          <div className="ringsign">
            <i className="live-dot" aria-hidden="true"></i> INTERACTIVE VISUAL
            METAPHOR · DEMO
          </div>
          <div className="globe-status" id="globe-status" aria-live="polite">
            Drag the globe · hover a marker · optionally show your approximate
            area
          </div>
          <div
            className="location-panel"
            aria-label="Optional approximate location on the globe"
          >
            <div className="location-row">
              <button
                type="button"
                className="location-action"
                id="locate-btn"
                aria-describedby="location-note"
              >
                ◎   Show my area
              </button>
              <button
                type="button"
                className="location-clear"
                id="clear-location"
                hidden
              >
                Clear
              </button>
            </div>
            <div
              className="location-note"
              id="location-note"
              role="status"
              aria-live="polite"
            >
              Off by default · browser permission needed · never saved or sent
              by this demo.
            </div>
          </div>
          <div className="globe-tools">
            <span className="globe-hint">Explore the globe</span>
            <button
              className="tool"
              id="rotate-btn"
              aria-pressed="true"
              title="Pause globe rotation"
              aria-label="Pause globe rotation"
            >
              Ⅱ
            </button>
            <button
              className="tool"
              id="zoom-in"
              title="Zoom into globe"
              aria-label="Zoom into globe"
            >
              +
            </button>
            <button
              className="tool"
              id="zoom-out"
              title="Zoom out of globe"
              aria-label="Zoom out of globe"
            >
              −
            </button>
            <button
              className="tool"
              id="reset-btn"
              title="Reset globe orientation"
              aria-label="Reset globe orientation"
            >
              ↺
            </button>
          </div>
          <div
            id="globeTip"
            className="globe-tip"
            role="tooltip"
            aria-hidden="true"
          >
            <strong></strong>
            <small></small>
          </div>
          <div className="scroll-note">Scroll to explore</div>
          <div className="scene-counter">
            <b id="sceneNo">01</b> / 04{" "}
            <span className="scene-dots" id="sceneDots">
              <span className="on"></span>
              <span></span>
              <span></span>
              <span></span>
            </span>
          </div>
        </div>
        <div className="chapter-layer">
          <article className="chapter is-current" data-scene="0" id="chapter-0">
            <div className="chapter-inner">
              <div className="eyebrow">Introducing the world of {brand}</div>
              <h1 className="h1">
                Your money.
                <br />
                <span>In perspective.</span>
              </h1>
              <p className="hero-desc">
                Every credit, purchase, transfer and investment tells a
                different story. See where your money really moves—and what
                still needs explaining.
              </p>
              <div className="hero-cta">
                <a href="#demo" className="primary">
                  Enter the sample experience <span className="arr">↗</span>
                </a>
                <a href="#flow" className="ghost-link">
                  Discover the idea <span className="arr">↘</span>
                </a>
              </div>
              <div className="chapter-index">01 — THE BIGGER PICTURE</div>
            </div>
          </article>
          <article className="chapter" data-scene="1" id="chapter-1">
            <div className="chapter-inner">
              <div className="eyebrow">01 / Understand the movement</div>
              <h2 className="chapter-title">
                Money moving <em>isn&apos;t</em> money spent.
              </h2>
              <p className="chapter-copy">
                A transfer between your own accounts is not another expense.{" "}
                {brand} is designed to help separate movement from actual
                consumption.
              </p>
              <div className="scene-tag">
                <i
                  className="dot"
                  style={{ background: "var(--blue)" } as CSSProperties}
                ></i>{" "}
                Internal transfers are distinct
              </div>
              <div className="chapter-index">02 — SEE THE DIFFERENCE</div>
            </div>
          </article>
          <article className="chapter" data-scene="2" id="chapter-2">
            <div className="chapter-inner">
              <div className="eyebrow">02 / Trust the details</div>
              <h2 className="chapter-title">
                Clarity starts with <em>questions.</em>
              </h2>
              <p className="chapter-copy">
                Not every bank narration makes sense. Unrecognized credits and
                uncertain categories should be flagged for your review—not
                silently guessed.
              </p>
              <div className="scene-tag">
                <i
                  className="dot"
                  style={{ background: "var(--gold)" } as CSSProperties}
                ></i>{" "}
                Unresolved items stay visible
              </div>
              <div className="chapter-index">03 — NOTHING HIDDEN</div>
            </div>
          </article>
          <article className="chapter" data-scene="3" id="chapter-3">
            <div className="chapter-inner">
              <div className="eyebrow">03 / From today to tax season</div>
              <h2 className="chapter-title">
                One clearer month.
                <br />
                <em>More prepared tomorrow.</em>
              </h2>
              <p className="chapter-copy">
                Organized evidence can support a tax-document checklist and a
                selected CA handoff later. It doesn&apos;t replace tax advice or
                filing.
              </p>
              <div className="scene-tag">
                <i
                  className="dot"
                  style={{ background: "var(--violet)" } as CSSProperties}
                ></i>{" "}
                Preparation, not tax-certification
              </div>
              <div className="chapter-index">04 — YOUR NEXT CHAPTER</div>
            </div>
          </article>
        </div>
      </section>
    </div>
  );
}
