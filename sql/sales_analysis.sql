/*
Sales Performance Dashboard — Microsoft SQL Server
Import data/sales_data.csv into dbo.SalesData before running.
Set OrderDate to DATE and numeric columns to suitable numeric types.
*/

-- 1. Preview and row count
SELECT TOP (10) * FROM dbo.SalesData;
SELECT COUNT(*) AS TotalRows, COUNT(DISTINCT OrderID) AS DistinctOrders
FROM dbo.SalesData;

-- 2. Duplicate order IDs
SELECT OrderID, COUNT(*) AS RowCount
FROM dbo.SalesData
GROUP BY OrderID
HAVING COUNT(*) > 1;

-- 3. KPI summary
SELECT
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit,
    COUNT(DISTINCT OrderID) AS TotalOrders,
    SUM(Quantity) AS UnitsSold,
    CAST(100.0 * SUM(Profit) / NULLIF(SUM(Sales), 0) AS DECIMAL(10,2)) AS ProfitMarginPct,
    CAST(1.0 * SUM(Sales) / NULLIF(COUNT(DISTINCT OrderID), 0) AS DECIMAL(12,2)) AS AverageOrderValue
FROM dbo.SalesData;

-- 4. Monthly trend
SELECT DATEFROMPARTS(YEAR(OrderDate), MONTH(OrderDate), 1) AS SalesMonth,
       SUM(Sales) AS TotalSales, SUM(Profit) AS TotalProfit,
       COUNT(DISTINCT OrderID) AS TotalOrders
FROM dbo.SalesData
GROUP BY DATEFROMPARTS(YEAR(OrderDate), MONTH(OrderDate), 1)
ORDER BY SalesMonth;

-- 5. Category performance
SELECT Category, SUM(Sales) AS TotalSales, SUM(Profit) AS TotalProfit,
       SUM(Quantity) AS UnitsSold
FROM dbo.SalesData
GROUP BY Category ORDER BY TotalSales DESC;

-- 6. Region performance
SELECT Region, SUM(Sales) AS TotalSales, SUM(Profit) AS TotalProfit,
       COUNT(DISTINCT OrderID) AS TotalOrders
FROM dbo.SalesData
GROUP BY Region ORDER BY TotalSales DESC;

-- 7. Top products
SELECT TOP (10) Product, SUM(Sales) AS TotalSales, SUM(Profit) AS TotalProfit,
       SUM(Quantity) AS UnitsSold
FROM dbo.SalesData
GROUP BY Product ORDER BY TotalSales DESC;

-- 8. Salesperson performance
SELECT Salesperson, SUM(Sales) AS TotalSales, SUM(Profit) AS TotalProfit,
       COUNT(DISTINCT OrderID) AS TotalOrders
FROM dbo.SalesData
GROUP BY Salesperson ORDER BY TotalSales DESC;

-- 9. Low/negative-profit transactions
SELECT OrderID, OrderDate, Product, Category, Region, Sales, Cost, Profit
FROM dbo.SalesData WHERE Profit <= 0 ORDER BY Profit ASC;

-- 10. Discount analysis
SELECT DiscountPct, COUNT(*) AS TransactionRows, SUM(Sales) AS TotalSales,
       SUM(Profit) AS TotalProfit,
       CAST(100.0 * SUM(Profit) / NULLIF(SUM(Sales), 0) AS DECIMAL(10,2)) AS ProfitMarginPct
FROM dbo.SalesData GROUP BY DiscountPct ORDER BY DiscountPct;
