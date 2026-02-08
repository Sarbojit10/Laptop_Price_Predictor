import pandas as pd

# Load the NEW dataset
# encoding='latin-1' helps read files with special characters (like Euro signs)
df = pd.read_csv('laptops_train.csv', encoding='latin-1')

print("--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- FIRST ROW (Sample Data) ---")
print(df.head(1))

print("\n--- INFO (Text or Numbers?) ---")
print(df.info())