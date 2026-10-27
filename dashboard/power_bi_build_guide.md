# Power BI Dashboard Build Guide

The Streamlit dashboard is runnable immediately. This guide helps you build an optional Power BI `.pbix` version.

## Import
1. Open Power BI Desktop.
2. Home → Get data → Text/CSV.
3. Select `data/sales_data.csv`, then Load.
4. Confirm `OrderDate` is Date type; `Sales`, `Cost`, `Profit`, `UnitPrice` are decimal/currency; `Quantity` is whole number.

## DAX measures
Create each via Modeling → New measure:

```DAX
Total Sales = SUM(SalesData[Sales])

Total Profit = SUM(SalesData[Profit])

Total Orders = DISTINCTCOUNT(SalesData[OrderID])

Units Sold = SUM(SalesData[Quantity])

Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)

Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)
```

## Suggested layout
- Header: Sales Performance Dashboard
- Cards: Total Sales, Total Profit, Total Orders, Profit Margin %
- Line chart: OrderDate by month; value = Total Sales
- Bar chart: Category by Total Sales
- Bar chart: Region by Total Sales
- Horizontal bar chart: Product by Total Sales; apply Top N = 10
- Slicers: OrderDate, Region, Category

Format sales/profit/AOV as currency and margin as percentage. Check KPI totals against SQL. Test slicers. Save as `dashboard/Sales_Performance_Dashboard.pbix`.
