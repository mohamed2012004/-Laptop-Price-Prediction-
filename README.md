# 💻 Laptop Price Prediction using Machine Learning

A machine learning project that predicts laptop prices based on specifications such as RAM, processor type, storage, and other technical features.

---

## 📁 Project Structure

Laptop-Price-Prediction/
│
├── artifacts/ # Contains saved models and tools
│ ├── label_encoder.pkl
│ ├── scaler.pkl
│ ├── model.pkl
│ └── metrics.json
│
├── model_development/ # Model building and preprocessing
│ └── model.py
│
├── model_evaluation/ # Model evaluation logic
│ └── evaluate.py
│
├── notebooks/ # EDA and data exploration
│ └── Laptop_Price_Analysis.ipynb
│
├── app.py # Streamlit web app for prediction
├── .gitignore # Git ignore file
└── README.md # Project overview and instructions

## 📊 Features
- **EDA:** Performed in Jupyter Notebook to understand trends and patterns in laptop pricing
- **Data Preprocessing:** Label Encoding and Scaling of features
- **Model Training:** Built using machine learning models (RandomForestRegressor and  GridSearchCV)
- **Model Evaluation:** Performance metrics saved in `metrics.json`
- **Deployment:** Interactive Streamlit web app for user-friendly prediction


### 🔗 Try the App

### 🔗 Try the App

You can try the deployed app live here:  
👉 [Click to Open Streamlit App](https://mohamed2012004--laptop-price-prediction--app-y62fya.streamlit.app/)
