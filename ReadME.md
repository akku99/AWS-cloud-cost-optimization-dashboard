# 📊 AWS Cloud Cost Optimization Analytics Dashboard

## 🚀 Project Overview

Organizations often struggle to monitor and optimize cloud spending across multiple AWS services.
This project analyzes AWS Cost Explorer data using Python, SQL, and Power BI to identify spending trends, major cost drivers, anomalies, and optimization opportunities.

---

## 🎯 Business Problem
Key challenges:
-Rising cloud expenditure
-Lack of visibility into service-level costs
-Difficulty identifying cost anomalies
-Inefficient resource utilization

## 📌 Solution
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

## 📌 Architecture Diagram

<img width="1280" height="720" alt="Architecture" src="https://github.com/user-attachments/assets/86140be8-5c67-43c3-aea6-0a685bc38758" />

## 🛠️  Technology Stack
Tools and their Purpose
1. Python -  ETL & Analysis
2. Pandas -  Data Processing
3. AWS Cost Explorer API - Cost Data
4. SQLite -  Data Storage
5. Power BI - Visualization
6. GitHub -  Version Control


## 🚀 Key Metrics
Total Spend
Monthly Spend
Maximum Spend
Service Share %
Month-over-Month Growth
Pareto Analysis

## 📸 Dashboard Preview
🔹Executive Overview
<img width="1303" height="730" alt="overview" src="https://github.com/user-attachments/assets/4caaf749-4f37-45e5-9876-11a9b386ce79" />

🔹Individual Service Share %
<img width="427" height="222" alt="Service share %" src="https://github.com/user-attachments/assets/8414c782-3b1b-4ff2-943a-6c85d5b4a274" />

🔹Pareto Analysis
<img width="438" height="421" alt="cumulative% of service_cost(pareto analysis)" src="https://github.com/user-attachments/assets/bb024b4b-2749-4f18-9978-a742163cf66e" />

🔹Total Cost vs Service Sjare %
<img width="432" height="430" alt="total cost vs service share %" src="https://github.com/user-attachments/assets/b2f0402a-b243-41db-aaa8-f1da8800ecd9" />


## 🚀 Key Insights

Example:
EC2 contributes 58% of total cloud spend.
Top 3 services account for 82% of spending.
Monthly spend increased 15% during Q4.
