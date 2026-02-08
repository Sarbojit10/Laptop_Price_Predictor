import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import pickle

# 1. Load the data
df = pd.read_csv('laptop_data.csv')

print("Loading data... Done!")

# 2. Separate Features (X) and Target (y)
# X is what we use to predict (Specs)
# y is what we want to predict (Price)
X = df.drop('Price', axis=1)
y = df['Price']

# 3. Split into Train and Test sets (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Build the Pipeline
# Step A: Convert 'Brand' from text to numbers
step1 = ColumnTransformer(transformers=[
    ('col_tnf', OneHotEncoder(sparse_output=False, drop='first'), ['Brand'])
], remainder='passthrough')

# Step B: The Brain (Linear Regression)
step2 = LinearRegression()

# Combine them into a pipe
pipe = Pipeline([
    ('step1', step1),
    ('step2', step2)
])

# 5. Train the model
print("Training the model...")
pipe.fit(X_train, y_train)

# 6. Check Accuracy
score = pipe.score(X_test, y_test)
print(f"Model Accuracy (R2 Score): {score:.4f}")

# 7. Save the model
pickle.dump(pipe, open('model.pkl', 'wb'))
print("Model saved as 'model.pkl'")