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
- End-to-end data pipeline creation (ETL/ELT)
- Python scripting for automation
- DuckDB as a fast, embedded analytical engine
- SQL transformations with DBT
- Exploratory Data Analysis (EDA) in Jupyter
- Power BI visualization and DAX modeling
- KPI creation: Return Rate, Customer Retention, CLV, Pareto














## Business Objectives





