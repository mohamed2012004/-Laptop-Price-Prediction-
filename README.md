# 💻 Laptop Price Prediction using Machine Learning

A machine learning project that predicts laptop prices based on specifications such as RAM, processor type, storage, and other technical features.

---

## 📁 Project Structure


│
├── artifacts/ # Contains saved models and tools
│ ├── label_encoder.pkl
│ ├── scaler.pkl
│ ├── model.pkl
│ └── metrics.json
│
├── model_development/
│ └── model.py # Code for preprocessing and training the model
│
├── model_evaluation/
│ └── evaluate.py # Code for evaluating the model
│
├── notebooks/
│ └── Laptop_Price_Analysis.ipynb # Exploratory Data Analysis notebook
│
├── app.py # Streamlit web application for deployment
├── .gitignore # Files and folders to ignore in version control
└── README.md # Project overview and documentation

## 📊 Features
- **EDA:** Performed in Jupyter Notebook to understand trends and patterns in laptop pricing
- **Data Preprocessing:** Label Encoding and Scaling of features
- **Model Training:** Built using machine learning models (RandomForestRegressor and  GridSearchCV)
- **Model Evaluation:** Performance metrics saved in `metrics.json`
- **Deployment:** Interactive Streamlit web app for user-friendly prediction


### 🔗 Try the App

You can try the deployed app live here:  
👉 [Click to Open Streamlit App]([https://laptop-price-predictor-mohammad.streamlit.app](https://mohamed2012004--laptop-price-prediction--app-y62fya.streamlit.app/))
