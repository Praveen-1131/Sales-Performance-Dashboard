import unittest
import pandas as pd
from src.analysis import calculate_kpis, monthly_summary, grouped_summary, data_quality_report

def sample_data():
    return pd.DataFrame({
        "OrderID": ["A", "B", "C"],
        "OrderDate": pd.to_datetime(["2025-01-03", "2025-01-20", "2025-02-02"]),
        "Sales": [100.0, 200.0, 50.0],
        "Profit": [20.0, 40.0, -5.0],
        "Quantity": [1, 2, 1],
        "Region": ["North", "South", "North"],
    })

class TestAnalysis(unittest.TestCase):
    def test_kpis(self):
        result = calculate_kpis(sample_data())
        self.assertEqual(result["total_sales"], 350.0)
        self.assertEqual(result["total_profit"], 55.0)
        self.assertEqual(result["total_orders"], 3)
        self.assertEqual(result["units_sold"], 4)
        self.assertAlmostEqual(result["profit_margin"], 55/350)
        self.assertAlmostEqual(result["average_order_value"], 350/3)

    def test_monthly_summary(self):
        result = monthly_summary(sample_data())
        self.assertEqual(len(result), 2)
        self.assertEqual(result.iloc[0]["Sales"], 300.0)

    def test_grouped_summary(self):
        result = grouped_summary(sample_data(), "Region")
        self.assertEqual(result.iloc[0]["Region"], "South")
        with self.assertRaises(ValueError):
            grouped_summary(sample_data(), "Missing")

    def test_quality_report(self):
        result = data_quality_report(sample_data())
        self.assertEqual(result["rows"], 3)
        self.assertEqual(result["duplicate_order_ids"], 0)

if __name__ == "__main__":
    unittest.main()
