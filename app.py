import streamlit as st
import pandas as pd
import pickle

# 1. Load the model and data
model = pickle.load(open('model.pkl', 'rb'))
df = pd.read_csv('laptop_data.csv')

# 2. Setup the Title
st.title("💻 Laptop Price Predictor")
st.write("Enter the laptop specs below to get an estimated price.")

# 3. Create the Input Form
# We use the dataframe to get the lists of Brands so we don't have to type them manually
brand = st.selectbox('Brand', df['Brand'].unique())

# Numeric inputs (We use the min and max from your data as limits)
ram = st.number_input('RAM (GB)', min_value=2, max_value=64, value=8)
storage = st.number_input('Storage Capacity (GB)', min_value=64, max_value=4096, value=512)
screen_size = st.number_input('Screen Size (Inches)', min_value=10.0, max_value=18.0, value=15.6)
weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=2.0)
processor_speed = st.number_input('Processor Speed (GHz)', min_value=1.0, max_value=5.0, value=2.5)

# 4. The "Predict" Button
if st.button('Predict Price'):
    # Create a dataframe with the user's inputs
    # MUST MATCH the column names you used in training!
    query = pd.DataFrame([[brand, processor_speed, ram, storage, screen_size, weight]],
                         columns=['Brand', 'Processor_Speed', 'RAM_Size', 'Storage_Capacity', 'Screen_Size', 'Weight'])
    
    # Ask the model to predict
    predicted_price = model.predict(query)
    
    # Show the result
    st.success(f"Estimated Price: ₹ {int(predicted_price[0])}")