# Sales Performance Dashboard — Complete Portfolio Project

A complete starter implementation for a fresher Data Analyst portfolio. It includes a synthetic dataset, Python analysis app, SQL Server queries, tests, and a Power BI build guide.

## Features
- Interactive dashboard built with Streamlit and Plotly
- KPI cards: sales, profit, orders, units sold, profit margin, average order value
- Monthly sales and profit trends
- Sales by category, region, and top products
- Filters for date range, region, and category
- CSV data validation and basic data-quality checks
- SQL Server analysis queries
- Power BI DAX measures and visual layout instructions

> The included 500-row dataset is synthetic and intended for learning/demo purposes, not real company reporting.

## Requirements
- Python 3.10 or newer
- SQL Server + SSMS only if you want to run the SQL queries
- Power BI Desktop only if you want to build the optional `.pbix` dashboard

## Run the Python dashboard (Windows / VS Code)
Open a terminal in this project folder:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Streamlit will show a local URL (usually `http://localhost:8501`) to open in your browser.

If you already have a virtual environment, activate it and run `pip install -r requirements.txt`.

## Project structure
```text
Sales-Performance-Dashboard-Full/
├── app.py
├── requirements.txt
├── data/sales_data.csv
├── src/analysis.py
├── sql/sales_analysis.sql
├── tests/test_analysis.py
├── dashboard/power_bi_build_guide.md
├── docs/data_dictionary.md
├── .gitignore
└── README.md
```

## Data fields
See `docs/data_dictionary.md`.

## SQL Server
Import `data/sales_data.csv` into SQL Server as `dbo.SalesData`, ensuring column names match. Then run `sql/sales_analysis.sql`.

## Power BI (optional)
Follow `dashboard/power_bi_build_guide.md`. The Streamlit app is runnable immediately; a Power BI `.pbix` file must be created and saved from Power BI Desktop.

## GitHub upload
From the project folder, initialize or use your existing repository and commit the project. If adding it to your existing Data-Analytics-Journey repository, copy this folder inside that repo, then run from the repo root:

```bash
git add Sales-Performance-Dashboard-Full
git commit -m "Add complete sales performance dashboard project"
git push origin master
```

## Resume bullet (use after running and understanding it)
**Sales Performance Dashboard | Python, SQL, Power BI, Streamlit**
- Developed an interactive dashboard to monitor sales, profit, order volume, profit margin, and average order value.
- Analyzed monthly trends and category, regional, and product performance using Python, Plotly, and SQL.
- Added date, region, and category filters to support focused business analysis.

Only list tools and outputs you actually used or built.
