# 💻 Laptop Price Prediction using Machine Learning

A machine learning project that predicts laptop prices based on specifications such as RAM, processor type, storage, and other technical features.

---

## 📁 Project Structure

notebooks/ — EDA and data exploration
 Laptop_Price_Analysis.ipynb

artifacts/ — Contains saved models and tools
1.1 label_encoder.pkl
1.2 scaler.pkl
1.3 model.pkl
1.4 metrics.json

model_development/ — Model building and preprocessing
2.1 model.py

model_evaluation/ — Model evaluation logic
3.1 evaluate.py


app.py — Streamlit web app for prediction

.gitignore — Git ignore file

README.md — Project overview and instructions

---

## 📊 Features

- **EDA:** Performed in Jupyter Notebook to understand trends and patterns in laptop pricing  
- **Data Preprocessing:** Label Encoding and Scaling of features  
- **Model Training:** Built using machine learning models (`RandomForestRegressor` and `GridSearchCV`)  
- **Model Evaluation:** Performance metrics saved in `metrics.json`  
- **Deployment:** Interactive Streamlit web app for user-friendly prediction  

---

### 🔗 Try the App

You can try the deployed app live here:  
👉 [Click to Open Streamlit App](https://mohamed2012004--laptop-price-prediction--app-y62fya.streamlit.app/)
