import streamlit as st
import pandas as pd
import pickle

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Laptop Price Predictor Pro",
    page_icon="💻",
    layout="wide"
)

# --- 2. CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp {background: linear-gradient(to right, #1e3c72, #2a5298); color: white;}
    .title-text {font-size: 50px; font-weight: bold; text-align: center; color: white;}
    .stButton>button {width: 100%; background-color: #ff4b4b; color: white; height: 50px; border-radius: 10px;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOAD DATA ---
try:
    model = pickle.load(open('model.pkl', 'rb'))
    df = pd.read_csv('laptops_data.csv')
    df.columns = df.columns.str.strip()
    df = df.fillna('Unknown')
except:
    st.error("Error: Missing 'model.pkl' or 'laptops_data.csv'")
    st.stop()

# --- 4. HEADER ---
st.markdown('<p class="title-text">💻 Laptop Price Predictor Pro</p>', unsafe_allow_html=True)
st.write("---")

# --- 5. TABS SYSTEM ---
# This splits the app into two pages
tab1, tab2 = st.tabs(["🔮 Prediction", "📊 Market Analysis"])

# ================= TAB 1: PREDICTION =================
with tab1:
    st.header("Customize Your Laptop")
    
    # Grid Layout
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        company = st.selectbox('Brand', df['Manufacturer'].unique())
        ram = st.selectbox('RAM', df['RAM'].unique())
        screen_size = st.selectbox('Screen Size', df['Screen Size'].unique())

    with col2:
        model_name = st.selectbox('Model Name', df['Model Name'].unique())
        storage = st.selectbox('Storage', df['Storage'].unique())
        screen = st.selectbox('Screen Type', df['Screen'].unique())

    with col3:
        type_name = st.selectbox('Laptop Type', df['Category'].unique())
        gpu = st.selectbox('GPU', df['GPU'].unique())
        cpu = st.selectbox('CPU', df['CPU'].unique())

    with col4:
        os = st.selectbox('OS', df['Operating System'].unique())
        os_version = st.selectbox('OS Version', df['Operating System Version'].unique())
        weight = st.selectbox('Weight', df['Weight'].unique())

    st.write("")
    st.write("")
    
    # Predict Button
    center_col1, btn_col, center_col2 = st.columns([1, 2, 1])
    with btn_col:
        if st.button('🚀 Predict Price'):
            query = pd.DataFrame([[company, model_name, type_name, screen_size, screen, cpu, ram, storage, gpu, os, os_version, weight]], 
                                 columns=['Manufacturer', 'Model Name', 'Category', 'Screen Size', 'Screen', 'CPU', 'RAM', 'Storage', 'GPU', 'Operating System', 'Operating System Version', 'Weight'])
            
            # Predict
            predicted_price = model.predict(query)
            actual_price = predicted_price[0] / 100
            
            st.success(f"💰 Estimated Price: ₹ {actual_price:,.2f}")
            st.balloons()

# ================= TAB 2: ANALYTICS =================
with tab2:
    st.header("Market Insights 📈")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("Average Price by Brand")
        # Group data by Brand and calculate average price (divided by 100 for Rupees)
        avg_price = df.groupby('Manufacturer')['Price'].mean().sort_values(ascending=False) / 100
        st.bar_chart(avg_price)
        
    with col_chart2:
        st.subheader("Price vs RAM")
        # Compare RAM size with Price
        ram_price = df.groupby('RAM')['Price'].mean().sort_values() / 100
        st.line_chart(ram_price)
        
    st.subheader("Operating System Distribution")
    st.bar_chart(df['Operating System'].value_counts())