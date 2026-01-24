"""import pandas as pd
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
print("output/sales_with_total.csv") """

# analyzer.py
import pandas as pd
from helper import calculate_total, format_currency

# Read data
df = pd.read_csv('data/sales.csv')

# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

# Add totals to our data
df['total'] = totals

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

# Show grand total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")

# understanding try : and except block in python
try:
    result = 10 / 0
except:
    print("hii there..!")