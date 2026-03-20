# End-to-End Retail Analytics Pipeline

## 🚀 Overview
This project demonstrates a complete data lifecycle, moving from raw data generation to actionable business insights. Instead of using static datasets, this system utilizes a custom-built Python engine to simulate a real-world retail environment.

## 🏗️ The Architecture
1. **Data Generation:** Python script using `Faker` to create relational CSVs (Sales & Products).
2. **ETL Layer:** Pandas cleans, transforms, and loads the data into a SQL relational database.
3. **Data Warehousing:** SQL (SQLite) serves as the "Source of Truth" with defined Fact and Dimension tables.
4. **Business Intelligence:** Power BI connects directly to the SQL layer to visualize KPIs like Revenue Growth and Product Performance.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas, SQLAlchemy, Faker
* **Database:** SQLite / SQL Server
* **Visualization:** Power BI (DAX)
