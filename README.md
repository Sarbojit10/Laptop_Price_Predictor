# 💻 Laptop Price Predictor Pro

A high-accuracy Machine Learning web application that estimates laptop prices based on 12 distinct hardware specifications.

**[🔴 Live Demo](PASTE_YOUR_STREAMLIT_LINK_HERE)**

![App Screenshot](IMAGE_PATH_HERE)
*(Upload a screenshot of your dashboard here to make it look professional)*

## 🚀 Key Features
* **Advanced AI Brain:** Powered by a **Random Forest Regressor** achieving **82.29% Accuracy** .
* **Smart Dashboard:** Features a clean, responsive UI with a "Tech Blue" gradient theme.
* **Real-Time Analytics:** Includes charts for market analysis (Brand vs. Price, RAM trends).
* **Live Currency Conversion:** Automatically converts predictive values from Paisa to Indian Rupees (₹).

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Python)
* **Machine Learning:** Scikit-Learn (Random Forest, Pipeline)
* **Data Processing:** Pandas, NumPy
* **Deployment:** Streamlit Cloud

## 📊 Project Workflow
1. **Data Ingestion:** Preprocessed a dataset of 977 laptops; implemented a 1/100 scaling factor to convert raw values from Paisa to Indian Rupees (INR) for realistic price estimation.
2. **Preprocessing:** Built a `ColumnTransformer` pipeline to handle One-Hot Encoding for 11 categorical variables.
3. **Modeling:** Trained a Random Forest Regressor (n_estimators=100) to capture non-linear pricing patterns.
4. **Deployment:** Hosted on Streamlit Cloud with CI/CD integration via GitHub.

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/Laptop_Price_Predictor.git](https://github.com/YourUsername/Laptop_Price_Predictor.git)
