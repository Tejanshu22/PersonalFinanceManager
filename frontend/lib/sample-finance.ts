import Decimal from "decimal.js";
import fixture from "../../docs/design/day05/sample-finance.json";

export type Classification = "unknown" | "transfer" | "income";
export function calculateSample(classification: Classification) {
  const totals = {
    income: new Decimal(0),
    consumption: new Decimal(0),
    gross_own_account_movement: new Decimal(0),
    unclassified_receipts: new Decimal(0),
    investments: new Decimal(0),
    card_repayments: new Decimal(0),
    selected_bank_cash_change: new Decimal(0),
  };
  const mapping = {
    income: "income",
    spending: "consumption",
    card_purchase: "consumption",
    own_transfer: "gross_own_account_movement",
    unknown: "unclassified_receipts",
    investment: "investments",
    card_repayment: "card_repayments",
  } as const;
  for (const row of fixture.rows) {
    const amount = new Decimal(row.amount);
    const kind =
      row.id === fixture.correction_target
        ? classification === "transfer"
          ? "own_transfer"
          : classification
        : row.classification;
    const key = mapping[kind as keyof typeof mapping];
    if (!key) throw new Error("Unsupported sample classification");
    totals[key] = totals[key].plus(amount.abs());
    if (row.source === "fictional-bank")
      totals.selected_bank_cash_change =
        totals.selected_bank_cash_change.plus(amount);
  }
  return Object.fromEntries(
    Object.entries(totals).map(([key, value]) => [key, value.toFixed(2)]),
  ) as Record<keyof typeof totals, string>;
}

// Keep paise exact through formatting: no conversion of money to Number.
export function money(value: string) {
  const amount = new Decimal(value);
  const [whole, fraction] = amount.abs().toFixed(2).split(".");
  const grouped = BigInt(whole).toLocaleString("en-IN");
  return `${amount.isNegative() && !amount.isZero() ? "−" : ""}₹${grouped}${fraction === "00" ? "" : `.${fraction}`}`;
}

export function barHeight(category: string) {
  const amount = fixture.rows
    .filter((row) => row.category === category)
    .reduce(
      (sum, row) => sum.plus(new Decimal(row.amount).abs()),
      new Decimal(0),
    );
  const categories = [
    ...new Set(
      fixture.rows
        .filter(
          (row) =>
            row.classification === "spending" ||
            row.classification === "card_purchase",
        )
        .map((row) => row.category),
    ),
  ];
  const maximum = categories.reduce(
    (max, key) =>
      Decimal.max(
        max,
        fixture.rows
          .filter((row) => row.category === key)
          .reduce(
            (sum, row) => sum.plus(new Decimal(row.amount).abs()),
            new Decimal(0),
          ),
      ),
    new Decimal(0),
  );
  return maximum.isZero()
    ? "0%"
    : `${amount.div(maximum).times(84).toFixed(2)}%`;
}
