import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
Faker.seed(42)

def generate_retail_data(num_products=50, num_sales=1000):

    products = []
    categories = ['Electronics', 'Home & Kitchen', 'Apparel', 'Books', 'Toys']
    
    for i in range(1, num_products + 1):
        products.append({
            'product_id': i,
            'product_name': fake.color_name() + " " + fake.word().capitalize(),
            'category': random.choice(categories),
            'base_price': round(random.uniform(10.0, 500.0), 2)
        })
    
    df_products = pd.DataFrame(products)


    sales = []
    for _ in range(num_sales):
        prod = random.choice(products)
        quantity = random.randint(1, 5)
        
        sales.append({
            'transaction_id': fake.uuid4(),
            'product_id': prod['product_id'], 
            'customer_name': fake.name(),
            'sale_date': fake.date_between(start_date='-1y', end_date='today'),
            'quantity': quantity,
            'total_amount': round(prod['base_price'] * quantity, 2),
            'store_location': fake.city()
        })
    
    df_sales = pd.DataFrame(sales)
    
    return df_products, df_sales

df_prods, df_sales = generate_retail_data()

print("--- Products Sample ---")
print(df_prods.head())
print("\n--- Sales Sample ---")
print(df_sales.head())


df_prods.to_csv('products.csv', index=False)
df_sales.to_csv('sales.csv', index=False)
