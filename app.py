from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st
from src.analysis import load_sales_data, calculate_kpis, monthly_summary, grouped_summary, data_quality_report

st.set_page_config(page_title="Sales Performance Dashboard", page_icon="📊", layout="wide")
ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "sales_data.csv"

@st.cache_data
def get_data():
    return load_sales_data(str(DATA_PATH))

def money(value):
    return f"${value:,.2f}"

st.title("📊 Sales Performance Dashboard")
st.caption("Interactive sales analytics demo • Synthetic sample data • 2025")

try:
    data = get_data()
except Exception as exc:
    st.error(f"Could not load the dataset: {exc}")
    st.stop()

with st.sidebar:
    st.header("Filters")
    min_date = data["OrderDate"].min().date()
    max_date = data["OrderDate"].max().date()
    date_range = st.date_input("Order date range", value=(min_date, max_date),
                               min_value=min_date, max_value=max_date)
    regions = sorted(data["Region"].dropna().unique().tolist())
    categories = sorted(data["Category"].dropna().unique().tolist())
    selected_regions = st.multiselect("Region", regions, default=regions)
    selected_categories = st.multiselect("Category", categories, default=categories)

filtered = data.copy()
if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range
    filtered = filtered[filtered["OrderDate"].dt.date.between(start_date, end_date)]
if selected_regions:
    filtered = filtered[filtered["Region"].isin(selected_regions)]
else:
    filtered = filtered.iloc[0:0]
if selected_categories:
    filtered = filtered[filtered["Category"].isin(selected_categories)]
else:
    filtered = filtered.iloc[0:0]

if filtered.empty:
    st.warning("No records match the selected filters. Select at least one region and category.")
    st.stop()

kpi = calculate_kpis(filtered)
c1, c2, c3 = st.columns(3)
c1.metric("Total Sales", money(kpi["total_sales"]))
c2.metric("Total Profit", money(kpi["total_profit"]))
c3.metric("Total Orders", f'{kpi["total_orders"]:,}')
c4, c5, c6 = st.columns(3)
c4.metric("Units Sold", f'{kpi["units_sold"]:,}')
c5.metric("Profit Margin", f'{kpi["profit_margin"]:.1%}')
c6.metric("Average Order Value", money(kpi["average_order_value"]))

st.divider()
monthly = monthly_summary(filtered)
left, right = st.columns(2)
with left:
    st.subheader("Monthly Sales Trend")
    fig = px.line(monthly, x="Month", y="Sales", markers=True, title="Sales by month")
    fig.update_layout(xaxis_title="", yaxis_title="Sales")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Sales by Category")
    category = grouped_summary(filtered, "Category")
    fig = px.bar(category, x="Category", y="Sales", color="Category", title="Revenue by category")
    fig.update_layout(showlegend=False, xaxis_title="", yaxis_title="Sales")
    st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)
with left:
    st.subheader("Regional Performance")
    region = grouped_summary(filtered, "Region")
    fig = px.bar(region, x="Region", y="Sales", color="Region", title="Revenue by region")
    fig.update_layout(showlegend=False, xaxis_title="", yaxis_title="Sales")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Top 10 Products")
    product = grouped_summary(filtered, "Product").head(10).sort_values("Sales")
    fig = px.bar(product, x="Sales", y="Product", orientation="h", title="Top products by revenue")
    fig.update_layout(xaxis_title="Sales", yaxis_title="")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Sales Data")
st.dataframe(filtered.sort_values("OrderDate", ascending=False), use_container_width=True, hide_index=True)

with st.expander("Data quality checks"):
    quality = data_quality_report(data)
    st.json(quality)
    st.caption("Duplicate OrderIDs are checked against transaction rows; this sample dataset is designed with one row per order.")

st.download_button("Download filtered data as CSV",
                   data=filtered.to_csv(index=False).encode("utf-8"),
                   file_name="filtered_sales_data.csv",
                   mime="text/csv")
