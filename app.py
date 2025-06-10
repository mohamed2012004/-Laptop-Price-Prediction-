import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Load model, scaler, and label encoder
with open('model_outputs/finalized_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model_outputs/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('model_outputs/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

st.title("💻 Laptop Price Prediction App")
st.divider()
st.write("Predict the price of a laptop based on its specifications.")
st.divider()

# User inputs (NO brand input)
processor_speed = st.number_input("Processor Speed (GHz)", value=2.50, step=0.50)
ram_size = st.number_input("RAM Size (GB)", value=16, step=4)
storage_capacity = st.number_input("Storage Capacity (GB)", value=512, step=128)

# Prediction trigger
st.divider()
predict_button = st.button("🔍 Estimate Price")
st.divider()

if predict_button:
    st.subheader("📊 Price Comparison Across Brands")

    brand_predictions = []
    for b in label_encoder.classes_:
        encoded_b = label_encoder.transform([b])[0]
        X_b = np.array([[processor_speed, ram_size, storage_capacity, encoded_b]])
        X_b_scaled = scaler.transform(X_b)
        pred = model.predict(X_b_scaled)[0]
        brand_predictions.append((b, pred))

    brand_df = pd.DataFrame(brand_predictions, columns=['Brand', 'Predicted Price ($)'])
    brand_df = brand_df.sort_values(by='Predicted Price ($)', ascending=False).reset_index(drop=True)

    # Show best brand as main prediction
    top_brand, top_price = brand_df.iloc[0]
    st.success(f"💰 Best estimated price: **${top_price:.2f}** for brand **{top_brand}**")

    st.dataframe(brand_df)
    st.bar_chart(data=brand_df.set_index('Brand'))
else:
    st.info("Click the button to estimate the laptop price.")
