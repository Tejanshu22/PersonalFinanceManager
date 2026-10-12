"use client";
import { useState, type CSSProperties } from "react";
import {
  calculateSample,
  money,
  barHeight,
  type Classification,
} from "../lib/sample-finance";
export function SampleDashboard({ brand }: { brand: string }) {
  const [classification, setClassification] =
    useState<Classification>("unknown");
  const totals = calculateSample(classification);
  const description = {
    unknown: "Waiting for classification",
    transfer: "You marked this as your own transfer",
    income: "You marked this as other income",
  }[classification];
  return (
    <section id="demo" className="section">
      <div className="demo-top reveal">
        <div>
          <div className="overline">Go beyond the animation</div>
          <h2>
            A real feeling.
            <br />
            <em>Fictional numbers.</em>
          </h2>
          <p className="lede">
            Explore a sample monthly report. Reclassify one unclear credit and
            see how the numbers change—without uploading anything.
          </p>
        </div>
        <span className="sample-label">
          100% fictional · no account required
        </span>
      </div>
      <div className="mock-app reveal" id="mockapp">
        <aside className="mock-side">
          <div className="side-title">{brand}</div>
          <p>Explore workspace</p>
          <span className="side-link active">◈   Overview</span>
          <span className="side-link">⇄   Transactions</span>
          <span className="side-link">▥   Reports</span>
          <span className="side-link">
            ▢   Tax readiness <small>· planned</small>
          </span>
          <span className="side-link">
            ⌁   CA sharing <small>· planned</small>
          </span>
          <div style={{ height: "90px" } as CSSProperties}></div>
          <p>
            Fictional demonstration
            <br />
            Not a connected account
          </p>
        </aside>
        <div className="mock-main">
          <div className="mock-head">
            <div>
              <div
                style={
                  {
                    font: "10px monospace",
                    letterSpacing: ".16em",
                    color: "#63867c",
                    marginBottom: "7px",
                  } as CSSProperties
                }
              >
                YOUR SAMPLE WORKSPACE
              </div>
              <h3>A month, made clearer.</h3>
            </div>
            <div className="date">
              <span className="sample-badge">Sample Data</span>
            </div>
          </div>
          <div className="coverage">
            <span aria-hidden="true">ⓘ</span>
            <div>
              <strong>Partial data coverage.</strong> This fictional report
              includes one selected bank account and an example card ledger. It
              cannot show your total net worth or true savings.
            </div>
          </div>
          <div className="metric-grid">
            <div
              className="metric"
              style={{ "--metric": "var(--mint)" } as CSSProperties}
            >
              <label>Recognized income</label>
              <strong id="income-total">{money(totals.income)}</strong>
              <small id="income-caption">
                {classification === "income"
                  ? "Includes reviewed credit"
                  : classification === "transfer"
                    ? "Own transfer excluded"
                    : "Excludes unknown credit"}
              </small>
            </div>
            <div
              className="metric"
              style={{ "--metric": "var(--coral)" } as CSSProperties}
            >
              <label>Consumption spending</label>
              <strong>{money(totals.consumption)}</strong>
              <small>Excludes repayments</small>
            </div>
            <div
              className="metric"
              style={{ "--metric": "var(--blue)" } as CSSProperties}
            >
              <label>Own-account transfers</label>
              <strong id="transfer-total">
                {money(totals.gross_own_account_movement)}
              </strong>
              <small>Not counted as spending</small>
            </div>
            <div
              className="metric"
              style={{ "--metric": "var(--gold)" } as CSSProperties}
            >
              <label>Unclassified receipts</label>
              <strong id="unknown-total">
                {money(totals.unclassified_receipts)}
              </strong>
              <small id="unknown-caption">
                {classification === "unknown"
                  ? "Needs your review"
                  : "No unresolved sample credit"}
              </small>
            </div>
          </div>
          <div className="report-grid">
            <div className="report-card">
              <div className="card-head">
                <h4>Spending by category</h4>
                <span>FICTIONAL EXAMPLE</span>
              </div>
              <div className="bars">
                <div className="bar-col">
                  <div
                    className="bar"
                    style={
                      {
                        height: barHeight("housing"),
                        "--bar": "#82b9a7",
                      } as CSSProperties
                    }
                  ></div>
                  <span>Housing</span>
                </div>
                <div className="bar-col">
                  <div
                    className="bar"
                    style={
                      {
                        height: barHeight("food"),
                        "--bar": "#9fc5f0",
                      } as CSSProperties
                    }
                  ></div>
                  <span>Food</span>
                </div>
                <div className="bar-col">
                  <div
                    className="bar"
                    style={
                      {
                        height: barHeight("utilities"),
                        "--bar": "#e7c188",
                      } as CSSProperties
                    }
                  ></div>
                  <span>Utilities</span>
                </div>
                <div className="bar-col">
                  <div
                    className="bar"
                    style={
                      {
                        height: barHeight("dining"),
                        "--bar": "#c0abe3",
                      } as CSSProperties
                    }
                  ></div>
                  <span>Dining</span>
                </div>
              </div>
            </div>
            <div className="report-card">
              <div className="card-head">
                <h4>What&apos;s different here?</h4>
                <span>NOT TAX ADVICE</span>
              </div>
              <div style={{ display: "grid", gap: "19px" } as CSSProperties}>
                <div style={{ display: "flex", gap: "13px" } as CSSProperties}>
                  <span style={{ color: "#5187ba" } as CSSProperties}>↔</span>
                  <div
                    style={
                      { fontSize: "12px", color: "#506a66" } as CSSProperties
                    }
                  >
                    <strong
                      style={
                        { display: "block", color: "#183b3a" } as CSSProperties
                      }
                    >
                      {money(totals.gross_own_account_movement)} own-account
                      movement
                    </strong>
                    Not another expense
                  </div>
                </div>
                <div style={{ display: "flex", gap: "13px" } as CSSProperties}>
                  <span style={{ color: "#9476d2" } as CSSProperties}>↗</span>
                  <div
                    style={
                      { fontSize: "12px", color: "#506a66" } as CSSProperties
                    }
                  >
                    <strong
                      style={
                        { display: "block", color: "#183b3a" } as CSSProperties
                      }
                    >
                      ₹9,000 investment contribution
                    </strong>
                    Tracked separately
                  </div>
                </div>
                <div style={{ display: "flex", gap: "13px" } as CSSProperties}>
                  <span style={{ color: "#c89346" } as CSSProperties}>?</span>
                  <div
                    style={
                      { fontSize: "12px", color: "#506a66" } as CSSProperties
                    }
                  >
                    <strong
                      style={
                        { display: "block", color: "#183b3a" } as CSSProperties
                      }
                    >
                      ₹3,600 incoming credit
                    </strong>
                    <span id="uncertain-sub">{description}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="txns">
            <div className="txns-header">
              <strong>Selected transactions</strong>
              <span>DEMONSTRATION ONLY</span>
            </div>
            <div className="tx-row">
              <div>
                <strong>Employer salary</strong>
                <div className="tx-sub">Recognized income</div>
              </div>
              <div>
                <span
                  className="status-pill"
                  style={
                    { background: "#e6f6ef", color: "#2c7560" } as CSSProperties
                  }
                >
                  Income
                </span>
              </div>
              <div className="tx-amount plus">+₹82,000</div>
            </div>
            <div className="tx-row">
              <div>
                <strong>Apartment rent</strong>
                <div className="tx-sub">Monthly expense</div>
              </div>
              <div>
                <span
                  className="status-pill"
                  style={
                    { background: "#fdeee7", color: "#995e49" } as CSSProperties
                  }
                >
                  Spending
                </span>
              </div>
              <div className="tx-amount out">−₹18,000</div>
            </div>
            <div className="tx-row">
              <div>
                <strong>Transfer to own bank</strong>
                <div className="tx-sub">Not consumption</div>
              </div>
              <div>
                <span
                  className="status-pill"
                  style={
                    { background: "#ebf3fd", color: "#4879a9" } as CSSProperties
                  }
                >
                  Transfer
                </span>
              </div>
              <div className="tx-amount out">−₹15,000</div>
            </div>
            <div className="tx-row">
              <div>
                <strong>Unrecognized incoming credit</strong>
                <div className="tx-sub" id="review-row-description">
                  {description}
                </div>
              </div>
              <div>
                <span className="status-pill" id="review-pill">
                  {classification === "unknown"
                    ? "Needs review"
                    : classification === "transfer"
                      ? "Transfer"
                      : "Income"}
                </span>
              </div>
              <div className="tx-amount plus">+₹3,600</div>
            </div>
          </div>
          <p className="sr-only" role="status">
            {description}. Recognized income {money(totals.income)}.
            Unclassified receipts {money(totals.unclassified_receipts)}.
          </p>
          <div className="review-panel">
            <div>
              <strong>What was the ₹3,600 credit?</strong>
              <p>Try changing the category; the recognized totals update.</p>
            </div>
            <div
              className="review-actions"
              role="group"
              aria-label="Classify sample credit"
            >
              <button
                data-classification="unknown"
                aria-pressed={classification === "unknown"}
                onClick={() => setClassification("unknown")}
              >
                Not sure
              </button>
              <button
                data-classification="transfer"
                aria-pressed={classification === "transfer"}
                onClick={() => setClassification("transfer")}
              >
                Own transfer
              </button>
              <button
                data-classification="income"
                aria-pressed={classification === "income"}
                onClick={() => setClassification("income")}
              >
                Other income
              </button>
            </div>
          </div>
          <p className="demo-remark">
            These figures are deterministic fictional examples. Real transaction
            classification will require supported imports, review and verified
            controls. An incoming credit alone does not establish tax treatment.
          </p>
        </div>
      </div>
    </section>
  );
}
