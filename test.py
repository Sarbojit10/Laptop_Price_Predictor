import pandas as pd

# Load the data
df = pd.read_csv('laptop_data.csv')

# 1. Check for missing values (nulls) and data types
print("--- INFO ---")
print(df.info())

# 2. Get a statistical summary (average price, min/max RAM, etc.)
print("\n--- DESCRIPTION ---")
print(df.describe())