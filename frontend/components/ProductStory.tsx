import type { CSSProperties } from "react";
export function ProductStory() {
  return (
    <section id="how" className="section">
      <div className="how-wrap">
        <div className="how-sticky reveal">
          <div
            className="overline"
            style={{ color: "var(--aqua)" } as CSSProperties}
          >
            From fragmented to familiar
          </div>
          <h2>
            Five steps.
            <br />
            <em>One clearer story.</em>
          </h2>
          <p className="lede" style={{ color: "#a7bdba" } as CSSProperties}>
            The end-to-end journey is a product plan. The interactive sample
            above is the only working data experience in this internal
            development preview.
          </p>
        </div>
        <div className="how-list reveal">
          <div className="how-item">
            <span className="how-num">01</span>
            <div>
              <h3>See before you share.</h3>
              <p>
                Explore a fictional month before choosing whether to use any
                future upload capability.
              </p>
            </div>
            <span className="next">↗</span>
          </div>
          <div className="how-item">
            <span className="how-num">02</span>
            <div>
              <h3>Import with intention.</h3>
              <p>
                Planned supported CSV/PDF formats, clear file limits and no bank
                credentials.
              </p>
            </div>
            <span className="next">↗</span>
          </div>
          <div className="how-item">
            <span className="how-num">03</span>
            <div>
              <h3>Correct the uncertain.</h3>
              <p>
                Review transfers, repayments, refunds and unclear credits before
                trusting a monthly report.
              </p>
            </div>
            <span className="next">↗</span>
          </div>
          <div className="how-item">
            <span className="how-num">04</span>
            <div>
              <h3>Understand the result.</h3>
              <p>
                See spending and cash movement separately, with explicit account
                and period coverage.
              </p>
            </div>
            <span className="next">↗</span>
          </div>
          <div className="how-item">
            <span className="how-num">05</span>
            <div>
              <h3>Prepare for tax season.</h3>
              <p>
                Eventually organize documents and share a selected package with
                your CA. Not filing or tax advice.
              </p>
            </div>
            <span className="next">↗</span>
          </div>
        </div>
      </div>
    </section>
  );
}
export function Trust() {
  return (
    <section id="trust" className="section">
      <div className="reveal">
        <div className="overline">Designed for confidence, not hype</div>
        <h2>
          Trust is not
          <br />
          <em>a visual effect.</em>
        </h2>
        <p className="lede">
          Beautiful interaction creates interest. Accurate calculations, visible
          uncertainty, appropriate controls and independent review must earn
          trust.
        </p>
      </div>
      <div className="trust-grid">
        <article className="trust-card reveal">
          <div className="top">
            <span>01 / CHOICE</span>
            <span className="trust-icon">◇</span>
          </div>
          <div>
            <h3>
              Sample first.
              <br />
              Data later.
            </h3>
            <p>
              Explore without uploading. Any real-document collection will
              remain unavailable until required security and privacy checks
              pass.
            </p>
          </div>
        </article>
        <article className="trust-card reveal">
          <div className="top">
            <span>02 / CLARITY</span>
            <span className="trust-icon">≈</span>
          </div>
          <div>
            <h3>
              Numbers with
              <br />
              context.
            </h3>
            <p>
              Separate transfers and investments from spending; reveal missing
              coverage and unresolved categories.
            </p>
          </div>
        </article>
        <article className="trust-card reveal">
          <div className="top">
            <span>03 / CONTROL</span>
            <span className="trust-icon">↗</span>
          </div>
          <div>
            <h3>
              Your records.
              <br />
              Your decision.
            </h3>
            <p>
              Planned scoped sharing and privacy settings need implementation
              and verification. Downloaded copies cannot be recalled.
            </p>
          </div>
        </article>
      </div>
    </section>
  );
}
export function Finale() {
  return (
    <section id="finale">
      <div className="final-inner reveal">
        <div className="eyebrow">A more understandable financial future</div>
        <h2>
          Less guessing.
          <br />
          <em>More knowing.</em>
        </h2>
        <p>
          Start with a fictional month and see how clear financial explanations
          could feel. No accounts, uploads or personal financial details
          required.
        </p>
        <div className="final-actions">
          <a href="#demo" className="primary">
            Explore the sample <span>↗</span>
          </a>
          <a href="#top" className="ghost-link">
            Return to the globe ↑
          </a>
        </div>
      </div>
    </section>
  );
}
export function Footer({ brand }: { brand: string }) {
  return (
    <footer className="footer">
      <div>
        <strong>{brand}</strong> · Provisional working name. Internal preview;
        planned features are not live.
      </div>
      <div>
        Interactive globe is a creative metaphor, not a live bank network.
        Approximate location is optional and stays within this demo page.
      </div>
      <div>
        Fictional finance data only. Optional approximate location stays in page
        memory; clear it anytime.
      </div>
    </footer>
  );
}
