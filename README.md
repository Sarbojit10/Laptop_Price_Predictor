# 💻 Laptop Price Predictor Pro

A high-accuracy Machine Learning web application that estimates laptop prices based on 12 distinct hardware specifications.

[🚀 Live Demo](https://laptop-price-predictor-v2.streamlit.app) ## ✨ Key Features
* **Advanced AI Brain:** Powered by a **Random Forest Regressor** achieving **82.29% Accuracy**.
* **Smart Dashboard:** Features a clean, responsive UI with a "Tech Blue" gradient theme.
* **Real-Time Analytics:** Includes interactive charts for market analysis (Brand vs. Price, RAM trends).
* **Live Currency Conversion:** Automatically converts raw dataset values from Paisa to Indian Rupees (INR).

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Python)
* **Machine Learning:** Scikit-Learn (Random Forest, Pipelines)
* **Data Processing:** Pandas, NumPy
* **Deployment:** Streamlit Cloud with CI/CD integration via GitHub

## 📊 Project Workflow
1.  **Data Ingestion:** Processed a dataset of 977 laptops with complex string-based features.
2.  **Preprocessing:** Built a `ColumnTransformer` pipeline to handle One-Hot Encoding for 11 categorical variables.
3.  **Modeling:** Trained a Random Forest Regressor (n_estimators=100) to capture non-linear pricing patterns.
4.  **Deployment:** Hosted on Streamlit Cloud with automated updates from GitHub main branch.

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/Sarbojit10/Laptop_Price_Predictor.git](https://github.com/Sarbojit10/Laptop_Price_Predictor.git)
