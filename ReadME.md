AWS Cloud Cost Optimization Analytics Dashboard
Project Overview

Organizations often struggle to monitor and optimize cloud spending across multiple AWS services.

This project analyzes AWS Cost Explorer data using Python, SQL, and Power BI to identify spending trends, major cost drivers, anomalies, and optimization opportunities.

Business Problem

Key challenges:

Rising cloud expenditure
Lack of visibility into service-level costs
Difficulty identifying cost anomalies
Inefficient resource utilization

Solution

Built an end-to-end analytics pipeline:

AWS Cost Explorer API
      ↓
Python ETL
      ↓
Data Cleaning
      ↓
SQLite Database
      ↓
Power BI Dashboard


Technology Stack
Tool	Purpose
Python	ETL & Analysis
Pandas	Data Processing
AWS Cost Explorer API	Cost Data
SQLite	Data Storage
Power BI	Visualization
GitHub	Version Control


Key Metrics
Total Spend
Monthly Spend
Maximum Spend
Service Share %
Month-over-Month Growth
Pareto Analysis

Dashboard Preview
Executive Summary

Cost Breakdown

Pareto Analysis

Forecasting

Key Insights

Example:

EC2 contributes 58% of total cloud spend.
Top 3 services account for 82% of spending.
Monthly spend increased 15% during Q4.
Forecast predicts 12% increase next quarter.
Multiple spending anomalies detected.