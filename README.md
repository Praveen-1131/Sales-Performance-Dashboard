# 📊 Sales Performance Dashboard

An interactive data analytics project built with **Python, Pandas, Streamlit, and Plotly** to analyze sales performance, track business KPIs, and visualize trends across products, categories, regions, and time periods.

🚀 **Live Demo:** [View Sales Performance Dashboard](https://sales-performance-dashboard-bsyk2bjuk4urccemo5enve.streamlit.app/)

💻 **GitHub Repository:** [Sales-Performance-Dashboard](https://github.com/Praveen-1131/Sales-Performance-Dashboard)

---

## 📌 Project Overview

Businesses need to understand their sales performance to make informed decisions. This project transforms sample sales data into useful information through interactive visualizations, key performance indicators (KPIs), and SQL analysis.

The dashboard helps users explore sales trends, compare regional performance, evaluate product categories, and investigate profitability using interactive filters.

## 🎯 Project Objectives

- Analyze overall sales and profit performance.
- Track important business performance indicators.
- Identify monthly sales trends.
- Compare sales across regions and product categories.
- Explore top-performing products.
- Investigate profitability and potential data quality issues.
- Present sales data through an interactive dashboard.

## ✨ Key Features

- **KPI Tracking:** Total Sales, Total Profit, Total Orders, Units Sold, Profit Margin, and Average Order Value.
- **Interactive Filters:** Filter sales data by order date, region, and product category.
- **Monthly Sales Trend:** Visualize sales performance over time.
- **Category Analysis:** Compare revenue across product categories.
- **Regional Analysis:** Explore differences in sales across regions.
- **Product Performance:** Identify top products by revenue.
- **Data Exploration:** View filtered sales records.
- **CSV Export:** Download filtered data for further analysis.
- **Data Quality Checks:** Inspect the dataset for potential data quality issues.
- **SQL Analysis:** Use SQL queries to investigate business performance.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Pandas | Data cleaning and analysis |
| Streamlit | Interactive dashboard development |
| Plotly | Interactive data visualizations |
| SQL | Business data analysis |
| Git | Version control |
| GitHub | Source code hosting |
| Visual Studio Code | Development environment |

## 📸 Dashboard Screenshots

Add screenshots of your running dashboard to showcase its interface and visualizations.

Create this folder in your project:

`docs/screenshots/`

Save your screenshots using these filenames:

- `dashboard-overview.png`
- `sales-analysis.png`

Then add them to the repository and keep the following Markdown:

### Dashboard Overview

![Sales Performance Dashboard Overview](docs/screenshots/dashboard-overview.png)

### Sales Analysis

![Sales Performance Analysis](docs/screenshots/sales-analysis.png)

*Note: Add the screenshot files to the specified folder so the images display correctly on GitHub.*

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
└── tests/
    └── test_analysis.py
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/Praveen-1131/Sales-Performance-Dashboard.git
```

### 2. Navigate to the project folder

```bash
cd Sales-Performance-Dashboard
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the dashboard

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

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

SQL scripts are available in:

`sql/sales_analysis.sql`

## 📁 Dataset

This project uses a **synthetic sample sales dataset** for demonstration and learning purposes. The data does not represent actual company transactions or confidential business information.

The dashboard uses the dataset to calculate KPIs, generate visualizations, and support interactive analysis.

## 🧪 Testing

The project includes a `tests` directory for analysis-related tests.

Run the tests using:

```bash
python -m pytest
```

## 💡 Skills Demonstrated

- Data cleaning and exploratory data analysis
- Business KPI development
- Sales and profitability analysis
- Python programming and Pandas
- Interactive dashboard development
- SQL querying and aggregation
- Data visualization
- Data interpretation and analytical thinking
- Git and GitHub version control
- Streamlit application deployment

## 🔮 Future Enhancements

- Connect the dashboard to a SQL database.
- Add sales forecasting and trend prediction.
- Expand customer and product performance analysis.
- Improve interactive filtering and visualizations.
- Add more automated data quality checks.

## 🌐 Live Application

Explore the deployed dashboard:

**[Sales Performance Dashboard — Live Demo](https://sales-performance-dashboard-bsyk2bjuk4urccemo5enve.streamlit.app/)**

## 👨‍💻 Author

**Praveen Venkata Bhargav**

B.Tech Computer Science and Engineering | Aspiring Data Analyst

- **GitHub:** [Praveen-1131](https://github.com/Praveen-1131)
- **Project Repository:** [Sales-Performance-Dashboard](https://github.com/Praveen-1131/Sales-Performance-Dashboard)
- **Live Demo:** [Open Dashboard](https://sales-performance-dashboard-bsyk2bjuk4urccemo5enve.streamlit.app/)

---

*This project was developed to practice data analytics, business KPI reporting, SQL, and interactive data visualization.*