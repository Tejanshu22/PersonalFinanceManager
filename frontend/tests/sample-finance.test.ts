import { test } from "node:test";
import assert from "node:assert/strict";
import fixture from "../../docs/design/day05/sample-finance.json";
import { calculateSample, money, barHeight } from "../lib/sample-finance";
for (const classification of ["unknown", "transfer", "income"] as const) {
  test(`exact totals for ${classification}; repayments and investments excluded from consumption`, () => {
    assert.deepEqual(
      calculateSample(classification),
      fixture.expectations[
        classification === "transfer" ? "own_transfer" : classification
      ],
    );
  });
}
test("corrections are reversible and never change fictional source rows", () => {
  const before = JSON.stringify(fixture);
  const original = calculateSample("unknown");
  calculateSample("income");
  calculateSample("transfer");
  assert.deepEqual(calculateSample("unknown"), original);
  assert.equal(JSON.stringify(fixture), before);
});
test("paise remain exact, including values beyond Number safe integer", () => {
  assert.equal(money("123456.01"), "₹1,23,456.01");
  assert.equal(money("-0.25"), "−₹0.25");
  assert.equal(money("9007199254740993.17"), "₹9,00,71,99,25,47,40,993.17");
  assert.equal(barHeight("housing"), "84.00%");
  assert.equal(barHeight("food"), "37.33%");
});
