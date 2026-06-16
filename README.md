# Nassau Candy Distributor – Product Line Profitability & Margin Performance Analysis

## Project Overview

This project analyzes product-level profitability, margin performance, and financial efficiency for Nassau Candy Distributor. The objective is to identify which products and divisions generate the highest profits, detect margin risks, and support data-driven business decisions regarding pricing, sourcing, promotions, and product portfolio management.

The project combines Data Cleaning, Exploratory Data Analysis (EDA), KPI computation, Profitability Analysis, Pareto Analysis, and an interactive Streamlit Dashboard.

---

## Problem Statement

High sales volume does not always translate into high profitability. Some products generate significant revenue but contribute little profit due to high production or operational costs.

The organization currently lacks visibility into:

* High-profit products
* High-margin products
* Low-margin risk products
* Division-wise financial performance
* Revenue versus profit contribution
* Product dependency and concentration risks

This project addresses these challenges through comprehensive profitability analytics.

---

## Dataset Information

### Dataset Name

Candy.csv

### Key Attributes

| Column         | Description                |
| -------------- | -------------------------- |
| Row ID         | Unique row identifier      |
| Order ID       | Unique order identifier    |
| Order Date     | Date of order              |
| Ship Date      | Date of shipment           |
| Ship Mode      | Shipping method            |
| Customer ID    | Unique customer identifier |
| Country/Region | Customer region            |
| City           | Customer city              |
| State/Province | Customer state             |
| Postal Code    | Customer postal code       |
| Division       | Product division           |
| Region         | Sales region               |
| Product ID     | Product identifier         |
| Product Name   | Product name               |
| Sales          | Total sales amount         |
| Units          | Quantity sold              |
| Gross Profit   | Sales minus cost           |
| Cost           | Manufacturing cost         |

---

## Project Objectives

### Product-Level Analysis

* Identify top profitable products
* Rank products by gross margin
* Detect high-sales low-margin products
* Analyze profit contribution by product

### Division-Level Analysis

* Compare revenue and profit by division
* Calculate division margin percentage
* Identify underperforming divisions

### Cost Diagnostics

* Analyze cost versus sales relationship
* Detect pricing inefficiencies
* Identify products requiring review

### Profit Concentration Analysis

* Perform Pareto (80/20) analysis
* Measure dependency on top-performing products
* Assess portfolio concentration risk

---

## Data Cleaning Process

The following data preparation steps were performed:

1. Removed duplicate records
2. Removed invalid sales records
3. Removed negative cost values
4. Handled missing unit values
5. Standardized product names
6. Standardized division names
7. Validated data consistency

---

## Key Performance Indicators (KPIs)

### Gross Margin (%)

Gross Margin (%) = (Gross Profit / Sales) × 100

### Profit Per Unit

Profit Per Unit = Gross Profit / Units

### Revenue Contribution

Revenue Contribution = Product Sales / Total Sales

### Profit Contribution

Profit Contribution = Product Profit / Total Profit

### Margin Volatility

Measures variation in profitability over time.

---

## Analytical Methodology

### Phase 1: Data Cleaning

* Missing value treatment
* Duplicate removal
* Data validation

### Phase 2: KPI Calculation

* Gross Margin %
* Profit Per Unit
* Revenue Contribution %
* Profit Contribution %

### Phase 3: Product Profitability Analysis

* Top products by profit
* Top products by margin
* Margin risk assessment

### Phase 4: Division Performance Analysis

* Revenue by division
* Profit by division
* Margin comparison

### Phase 5: Pareto Analysis

* Products generating 80% of revenue
* Products generating 80% of profit
* Dependency assessment

### Phase 6: Cost Structure Diagnostics

* Cost vs Sales analysis
* Margin risk detection
* Pricing review opportunities

---

## Technologies Used

### Programming Language

* Python 3.x

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Streamlit

### Development Environment

* Jupyter Notebook
* VS Code

---

## Project Structure

```text
Nassau-Candy-Analysis/
│
├── data/
│   └── Candy.csv
│
├── notebooks/
│   └── Profitability_Analysis.ipynb
│
├── dashboard/
│   └── app.py
│
├── outputs/
│   ├── Cleaned_Candy_Data.csv
│   ├── Product_Profitability.csv
│   ├── Division_Performance.csv
│   └── Pareto_Analysis.csv
│
├── README.md
│
└── requirements.txt
```

---

## Streamlit Dashboard Features

### Product Profitability Dashboard

* Product margin leaderboard
* Top profit products
* Profit contribution charts

### Division Performance Dashboard

* Revenue vs Profit comparison
* Margin distribution by division

### Cost Diagnostics Dashboard

* Cost vs Sales scatter plots
* Margin risk indicators

### Pareto Dashboard

* Revenue concentration analysis
* Profit concentration analysis
* Dependency indicators

---

## User Controls

* Date Range Filter
* Division Filter
* Product Search
* Margin Threshold Slider

---

## Expected Business Impact

This project enables Nassau Candy Distributor to:

* Improve profitability visibility
* Optimize pricing strategies
* Reduce margin leakage
* Identify cost inefficiencies
* Prioritize high-value products
* Reduce dependency on a small set of products
* Improve strategic decision-making

---

## Future Enhancements

* Demand Forecasting
* Customer Profitability Analysis
* Factory-Level Performance Analysis
* Geographic Profitability Mapping
* Automated Margin Risk Alerts
* Machine Learning Profit Prediction

---

## Conclusion

The Product Line Profitability & Margin Performance Analysis provides a comprehensive understanding of Nassau Candy Distributor’s financial performance. By combining profitability metrics, division analysis, cost diagnostics, and Pareto analysis, the organization gains actionable insights that support sustainable growth, improved margins, and data-driven business decisions.
