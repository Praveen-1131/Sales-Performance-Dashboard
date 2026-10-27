# 📊 Sales Performance Dashboard

An interactive data analytics project designed to analyze sales performance, track business KPIs, and identify trends across products, categories, regions, and time periods.

Built using **Python, Pandas, Streamlit, SQL, and Power BI dashboard development concepts**, this project demonstrates an end-to-end approach to sales data analysis and visualization.

## 🚀 Project Overview

Businesses need to understand their sales performance to make informed decisions. This project transforms sample sales data into meaningful insights through interactive visualizations, key performance indicators (KPIs), and SQL analysis.

The dashboard helps users explore sales trends, compare regional performance, evaluate product profitability, and investigate the impact of discounts.

## 🎯 Project Objectives

- Analyze overall sales and profit performance.
- Track key business performance indicators.
- Identify monthly sales trends.
- Compare sales across regions and product categories.
- Evaluate product and salesperson performance.
- Investigate discounts and low-profit transactions.
- Present insights through interactive dashboards.

## ✨ Key Features

- **KPI Tracking:** Total Sales, Total Profit, Total Orders, Units Sold, Profit Margin, and Average Order Value.
- **Interactive Filters:** Filter sales data by date, region, and category.
- **Sales Trend Analysis:** Visualize monthly sales performance.
- **Category Analysis:** Compare performance across product categories.
- **Regional Analysis:** Identify differences in sales and profitability across regions.
- **Product Performance:** Analyze top-performing products.
- **Data Exploration:** View filtered sales records and download the data as a CSV file.
- **Data Quality Checks:** Inspect the dataset for potential data quality issues.
- **SQL Analysis:** Explore business questions using SQL queries.
- **Power BI Guide:** Follow the included guide to build a Power BI report.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Data Analysis:** Pandas
- **Dashboard Development:** Streamlit
- **Data Visualization:** Plotly
- **Database Querying:** SQL / SQL Server-compatible queries
- **Business Intelligence:** Microsoft Power BI (report-building guide included)
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

## 📂 Project Structure

```text
Sales-Performance-Dashboard/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── sales_data.csv
├── src/
│   ├── __init__.py
│   └── analysis.py
├── sql/
│   └── sales_analysis.sql
├── dashboard/
│   └── power_bi_build_guide.md
├── docs/
│   └── data_dictionary.md
└── tests/
    └── test_analysis.py
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Praveen-1131/Sales-Performance-Dashboard.git
```

### 2. Open the project folder

```bash
cd Sales-Performance-Dashboard
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the dashboard

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

`http://localhost:8501`

## 🧮 SQL Analysis

The SQL scripts demonstrate how to investigate business performance using queries for:

- Overall sales and profit KPIs
- Monthly sales trends
- Category-wise performance
- Region-wise sales
- Top-performing products
- Salesperson performance
- Low-profit transactions
- Discount analysis

SQL queries are available in `sql/sales_analysis.sql`.

## 📈 Power BI Dashboard

The project includes a Power BI build guide at:

`dashboard/power_bi_build_guide.md`

Use the guide and the supplied CSV dataset to create a Power BI report with KPI cards, sales trend charts, category and regional comparisons, and interactive filters.

**Note:** The Power BI `.pbix` report is not included yet. It must be created separately in Power BI Desktop.

## 🧪 Testing

Run the project's unit tests with:

```bash
python -m pytest
```

## 📁 Dataset

The project uses a **synthetic sample sales dataset** for demonstration and learning purposes. It does not represent actual company transactions or confidential business information.

## 💡 Skills Demonstrated

- Data cleaning and exploratory data analysis
- Business KPI development
- Sales and profitability analysis
- Python programming and Pandas
- Interactive dashboard development
- SQL querying and aggregation
- Data visualization
- Data interpretation and business problem-solving
- Git and GitHub project management

## 🔮 Future Enhancements

- Add a completed Power BI report.
- Connect the dashboard to a SQL database.
- Add sales forecasting and trend prediction.
- Implement more advanced customer and product analysis.
- Deploy the Streamlit dashboard online.

## 👨‍💻 Author

**Praveen Venkata Bhargav**

B.Tech Computer Science and Engineering | Aspiring Data Analyst

GitHub: [Praveen-1131](https://github.com/Praveen-1131)

---

If you find this project useful, feel free to explore the repository and its analysis scripts.
