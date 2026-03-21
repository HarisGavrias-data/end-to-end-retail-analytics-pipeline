import pandas as pd 
from sqlalchemy import create_engine

sales = pd.read_csv('sales.csv')
products = pd.read_csv('products.csv')
# Turning date into datetime object
sales['sale_date'] = pd.to_datetime(sales['sale_date'], errors = 'coerce')
# Checking for Null
print(products.isna().sum(),sales.isna().sum()) 
# Joining tables to calculate net profit
sales_products = pd.merge(sales, products, on='product_id', how='left')
sales_products['gross_profit'] = sales_products['total_amount'] - (0.7* sales_products['base_price'] * sales_products['quantity'])
sales_products['net_profit'] = sales_products['gross_profit'] * 0.9
# Adding the calculated columns from the merge back to the sales table
sales['gross_profit'] = sales_products['gross_profit']
sales['net_profit'] = sales_products['net_profit']
# 1. Defining Connection Details
# Format: mysql+pymysql://user:password@host:port/database_name
user = 'root'
password = 'your_db_password' # different for everyone
host = 'localhost'
port = '3306'
db_name = 'retail_analytics' # create this database in Workbench first

# 2. Creating the Engine
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}")

# 3. Load DataFrames to MySQL
# Sending the original 'products' and the updated 'sales' (with profit columns)
products.to_sql('dim_products', con=engine, if_exists='replace', index=False)
sales.to_sql('fact_sales', con=engine, if_exists='replace', index=False)

print("Data loaded into MySQL Workbench")


