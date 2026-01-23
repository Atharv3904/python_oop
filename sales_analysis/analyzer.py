import pandas as pd
import os
import json

df = pd.read_csv('data/sales.csv')
print(df)

print(f"\n shape :{df.shape[0]} rows , {df.shape[1]} columns")
df['total'] = df['quantity'] * df['price']
print(df)

os.makedirs('output', exist_ok=True)

df.to_json('output/sales_with_total.json', orient='records', lines=True)

df.to_excel('output/sales_data.xlsx', index=False)
df.to_csv('output/sales_with_total.csv', index=False)  

print("file saved successfully ")

print("output/sales_with_total.json")
print("output/sales_data.xlsx")
print("output/sales_with_total.csv")