import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sys
import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(BASE_DIR))

# Model imports
from inference.predict_freight import predict_freight_cost
from inference.predict_invoice import predict_invoice_flag

# Page Configuration
st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    page_icon="📦",
    layout="wide"
)

# Header
st.title("📦 Vendor Invoice Intelligence Portal")
st.subheader("AI-Driven Freight Cost Prediction & Invoice Risk Flagging")

st.markdown("""
This portal helps:
- Predict freight cost with advanced ML models
- Detect risky invoices automatically
- Improve finance operations
""")

st.divider()

# Sidebar
st.sidebar.title("🔍 Model Selection")
selected_model = st.sidebar.radio(
    "Choose Prediction Module",
    [
        "Freight Cost Prediction",
        "Invoice Manual Approval Flag"
    ]
)

st.sidebar.markdown("""
### 📊 Business Impact
- 📈 Improved cost forecasting
- 🛑 Reduced invoice fraud & anomalies
- ⚡ Faster finance operations
""")

# Freight Cost Prediction
if selected_model == "Freight Cost Prediction":
    st.subheader("🚚 Freight Cost Prediction")
    
    st.markdown("""
    **Objective:**
    Predict freight cost using invoice dollar value to support
    budgeting, cost optimization, and vendor negotiation.
    """)
    
    model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models", "predict_freight_model.pkl")
    
    if not os.path.exists(model_path):
        st.error(f"Model file not found at: {model_path}")
    else:
        with open(model_path, 'rb') as f:
            model = joblib.load(f)

        with st.form("freight_form"):
            dollars = st.number_input(
                "💰 Invoice Dollars",
                min_value=1.0,
                value=18500.0
            )
            submit_freight = st.form_submit_button("🔮 Predict Freight Cost")

        if submit_freight:
            try:
                input_data = {"Dollars": [dollars]}
                prediction = predict_freight_cost(input_data)['Predicted_Freight']
                st.success("Prediction completed successfully")
                st.metric(
                    label="📊 Estimated Freight Cost",
                    value=f"${prediction[0]:,.2f}"
                )
            except Exception as e:
                st.error(f"Error: {e}")

# Invoice Risk Prediction
elif selected_model == "Invoice Manual Approval Flag":
    st.subheader("🧾 Invoice Risk Prediction")
    
    st.markdown("""
    **Objective:**
    Identify invoices that require manual approval using ML-based risk detection.
    """)

    with st.form("invoice_form"):
        invoice_quantity = st.number_input("Invoice Quantity", min_value=1, value=100)
        invoice_dollars = st.number_input("Invoice Dollars", min_value=1.0, value=2000.0)
        freight = st.number_input("Freight", min_value=1.0, value=500.0)
        total_item_quantity = st.number_input("Total Item Quantity", min_value=1, value=150)
        total_item_dollars = st.number_input("Total Item Dollars", min_value=1.0, value=2476.0)

        submit_flag = st.form_submit_button("🧠 Evaluate Invoice Risk")

    if submit_flag:
        try:
            input_data = {
                "invoice_quantity": [invoice_quantity],
                "invoice_dollars": [invoice_dollars],
                "Freight": [freight],
                "total_item_quantity": [total_item_quantity],
                "total_item_dollars": [total_item_dollars]
            }
            flag_prediction = predict_invoice_flag(input_data)['Predicted_Flag']
            if bool(flag_prediction[0]):
                st.error("🚨 Manual Approval Required")
            else:
                st.success("✅ Safe for Auto-Approval")
        except Exception as e:
            st.error(f"Error: {e}")
