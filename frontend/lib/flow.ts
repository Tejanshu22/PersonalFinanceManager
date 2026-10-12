export const flowMeta = {
  income: {
    heading: "Money that comes in.",
    copy: "Salary and recognized income can be tracked without assuming that every incoming bank credit is taxable income.",
    color: "#8bdbc0",
  },
  spending: {
    heading: "See what you actually spent.",
    copy: "Groceries, housing and services belong in spending. A card repayment does not create a second purchase.",
    color: "#eead93",
  },
  transfers: {
    heading: "Movement is not consumption.",
    copy: "Money moving between accounts you own should remain visible without inflating your expenses.",
    color: "#87bbf6",
  },
  investments: {
    heading: "Your money, put to work.",
    copy: "An investment contribution is a distinct cash flow—not the same thing as routine spending or a guaranteed return.",
    color: "#bca4ee",
  },
  review: {
    heading: "Some stories need your input.",
    copy: "An unknown credit must stay unresolved until you review it. Source information and corrections matter more than confident guesses.",
    color: "#e8cc86",
  },
} as const;
export type FlowKey = keyof typeof flowMeta;
