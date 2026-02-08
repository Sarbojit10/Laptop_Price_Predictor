import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor # <--- NEW ALGORITHM
from sklearn.metrics import r2_score
import pickle

# 1. Load Data
df = pd.read_csv('laptops_data.csv')
df.columns = df.columns.str.strip()
df = df.fillna('Unknown')

# 2. Separate Inputs (X) and Output (y)
X = df.drop('Price', axis=1)
y = df['Price']

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Preprocessing (The Translator)
step1 = ColumnTransformer(transformers=[
    ('col_tnf', OneHotEncoder(sparse_output=False, drop='first', handle_unknown='ignore'), 
     ['Manufacturer', 'Model Name', 'Category', 'Screen Size', 'Screen', 'CPU', 'RAM', 'Storage', 'GPU', 'Operating System', 'Operating System Version', 'Weight'])
], remainder='passthrough')

# 5. The Model (Random Forest)
# n_estimators=100 means we are using 100 "Decision Trees" to decide the price
step2 = RandomForestRegressor(n_estimators=100,
                              random_state=42,
                              max_samples=0.5,
                              max_features=0.75,
                              max_depth=15)

# 6. Pipeline
pipe = Pipeline([
    ('step1', step1),
    ('step2', step2)
])

# 7. Train
print("Training with Random Forest (This might take 5-10 seconds)...")
pipe.fit(X_train, y_train)

# 8. Evaluate
y_pred = pipe.predict(X_test)
score = r2_score(y_test, y_pred)
print(f"🚀 New Model Accuracy: {score:.4f}")

# 9. Save
pickle.dump(pipe, open('model.pkl', 'wb'))
print("Saved better model as 'model.pkl'")