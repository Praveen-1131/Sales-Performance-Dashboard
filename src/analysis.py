"""Reusable sales dashboard calculations and data validation."""
from __future__ import annotations
import pandas as pd

REQUIRED_COLUMNS = {
    "OrderID", "OrderDate", "Customer", "Product", "Category", "Region",
    "City", "Salesperson", "Quantity", "UnitPrice", "DiscountPct",
    "Sales", "Cost", "Profit"
}

def load_sales_data(path: str) -> pd.DataFrame:
    """Load CSV, validate required columns, and normalize data types."""
    df = pd.read_csv(path)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {', '.join(sorted(missing))}")
    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    numeric = ["Quantity", "UnitPrice", "DiscountPct", "Sales", "Cost", "Profit"]
    for col in numeric:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["OrderID", "OrderDate", "Sales", "Profit", "Quantity"])
    return df

def calculate_kpis(df: pd.DataFrame) -> dict:
    """Calculate core business KPIs for a filtered transaction dataframe."""
    total_sales = float(df["Sales"].sum())
    total_profit = float(df["Profit"].sum())
    orders = int(df["OrderID"].nunique())
    units = int(df["Quantity"].sum())
    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "total_orders": orders,
        "units_sold": units,
        "profit_margin": (total_profit / total_sales) if total_sales else 0.0,
        "average_order_value": (total_sales / orders) if orders else 0.0,
    }

def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales/profit by calendar month."""
    if df.empty:
        return pd.DataFrame(columns=["Month", "Sales", "Profit", "Orders"])
    out = df.assign(Month=df["OrderDate"].dt.to_period("M").dt.to_timestamp())
    return (out.groupby("Month", as_index=False)
            .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"),
                 Orders=("OrderID", "nunique"))
            .sort_values("Month"))

def grouped_summary(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Aggregate sales, profit, quantity by a requested dimension."""
    if group_col not in df.columns:
        raise ValueError(f"Unknown grouping column: {group_col}")
    return (df.groupby(group_col, as_index=False)
            .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"),
                 Units=("Quantity", "sum"))
            .sort_values("Sales", ascending=False))

def data_quality_report(df: pd.DataFrame) -> dict:
    """Return useful checks for the dataset."""
    return {
        "rows": int(len(df)),
        "duplicate_order_ids": int(df["OrderID"].duplicated().sum()),
        "missing_cells": int(df.isna().sum().sum()),
        "negative_sales_rows": int((df["Sales"] < 0).sum()),
        "nonpositive_quantity_rows": int((df["Quantity"] <= 0).sum()),
    }
