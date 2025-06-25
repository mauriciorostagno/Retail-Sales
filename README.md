# Retail Sales
![](images/retail-sales-introduction.png)

---
<img src="images/matplotlib-logo.png" alt="Matplotlib Logo" width="130"/> <img src="images/numpy-logo.png" alt="Numpy Logo" width="130"/> <img src="images/pandas-logo.jpg" alt="Pandas Logo" width="130"/> <img src="images/atom-logo.png" alt="Streamlit Logo" width="130"/> <img src="images/jupyter-logo.png" alt="Jupyter Logo" width="130"/> <img src="images/dax-logo.png" alt="Dax Logo" width="130"/> <img src="images/powerbi-logo.png" alt="Power BI Logo" width="130"/> <img src="images/duckdb-logo.png" alt="DuckDB Logo" width="130"/>

## Introduction
This project focuses on analyzing transactional data from a retail store to discover business performance insights. The main goal is to evaluate operational and marketing metrics using a full data pipeline — from extraction to visualization — and a dynamic Power BI dashboard powered by DuckDB and SQL transformations.
The final goal is to support the CEO and CMO in making informed decisions by presenting revenue indicators, customer segments, return trends, and time-based performance based on transactional data of the fiscal year in question.

## Problem Statement
Retailers use to face the challenge of handling a large quantity of data without transforming it into business value. In this project, the company looks for:

- A deep understanding of revenue sources.
- Identification of top-performing products, customers, and countries.
- Clear metrics around returns and customer retention.
- A dashboard that provides both operational and marketing perspectives.

This project addresses those needs through an end-to-end pipeline and a data storytelling dashboard, made for long-term planning.

## Business Objectives
### Revenue Analysis
Revenue streams were analyzed by analyzing product performance, customer segments, key sales and return indicators, and contribution by country.
### Customer Insights
Measure customer retention analyzed, top buyers, revenue concentration (Pareto), and calculate a basic Customer Lifetime Value (CLV) to support acquisition and loyalty strategies.
### Time-Based Performance
All indicators and important information about trends in times when customers interact most and least with the company.

## Project Pipeline

### Data Extraction
- Dataset named "tata-online-retail-dataset" downloaded from Kaggle using the Kaggle API.
- API key created in the official website and kaggle.json configured manually on local environment.
- Python file named "extract.py".

### Loading into DuckDB
- CSV file loaded and transformed into a DuckDB database.
- Cleaned and structured using Python scripts.
- Python file named "load_to_duckdb.py"

### Transformation with DBT (SQL)
- Business logic applied through SQL-based transformations (e.g., "country" column data changed using CASE WHEN logic)
- Also in python file named "load_to_duckdb.py"

### Exploratory Analysis (EDA)
- Conducted in Jupyter Notebook to validate and explore variables like sales trends, returns, customer behavior and correlations between data.

### Dashboard in Power BI
- Dataset exported in PBIX format, as I do not have a premium account.
- Dashboard designed for executive-level storytelling, different pages and performance indicators.

## Skills / Concepts Demonstrated
- End-to-end data pipeline creation (ETL/ELT).
- Python scripting for automation.
- DuckDB as a fast, embedded analytical engine.
- SQL transformation with DBT for practice.
- Exploratory Data Analysis (EDA) in Jupyter Notebook.
- Power BI visualization and DAX modeling
- KPI creation: Return Rate, Customer Retention, CLV, Pareto, Peak Sales Hour, Top 5% Revenue, etc.

## Modelling
<img src="images/model.png" alt="Schema" width="630"/>
The model is a star schema. There are 1 dimension table (df), 1 calendar table and 2 fact table made only for different graphs and KPI's.

## Visualization

The report consists in 1 front page and 3 sections with different information.

Page name: Front Page
<img src="images/dashboard-frontpage.png" alt="Front Page" width="930"/>

Page name: Sales Overview
<img src="images/dashboard-salespage.png" alt="Sales Page" width="930"/>

Page name: Customer Insights
<img src="images/dashboard-customerpage.png" alt="Customer Page" width="930"/>

Page name: Time-Based Performance
<img src="images/dashboard-timepage.png" alt="Time Page" width="930"/>

## Dashboard Features - Key Components

1. Revenue KPIs

   - Total Revenue, Average revenue per Customer (ARPC), and Top 5 Products by Revenue

    `total_sales_value = 
CALCULATE(
    SUM('df'[total_income]),
    'df'[quantity] > 0
  )`

2. Return Rate Analysis

   - Percentage of returned products (units and rate), financial impact visualized

   `total_returns_value = 
CALCULATE(
    ABS(SUM('df'[total_income])),
    'df'[quantity] < 0
)`
   
3. Customer Retention

   - One-time vs. repeat buyer ratio and Order frecuency throughout the year
   
   `customer_retention_rate = 
VAR TotalCustomers =
    CALCULATE(
        DISTINCTCOUNT('df'[id_customer])
    )
VAR RepeatCustomers =
    CALCULATE(
        DISTINCTCOUNT('df'[id_customer]),
        FILTER(
            'df',
            CALCULATE(COUNTROWS('df'), ALLEXCEPT('df', 'df'[id_customer])) > 1
        )
    )
RETURN DIVIDE(RepeatCustomers, TotalCustomers)`
   
   `order_frequency = 
DIVIDE([total_orders], [unique_customers])`
   
4. Top 5% Customers
   - High-value quantity of customers identified
     
     `top_5%_customers_count = 
VAR CustomerTable =
    SUMMARIZE(
        'df',
        'df'[id_customer],
        "total_income", SUM('df'[total_income])
    )
VAR Percentile95 =
    PERCENTILEX.INC(CustomerTable, [total_income], 0.95)
RETURN
    COUNTROWS(
        FILTER(
            CustomerTable,
            [total_income] >= Percentile95
        )
    )
`
   
9. Pareto 80/20 Analysis
    -
   
11. Customer Lifetime Value (Simple Model)
    -
    
13. Time-Based Sales Trends
    -
    
15. Geographical Insights
    -
    
17. as





## Findings and Insights

## Conclusion & Recommendations











