import os
import joblib
import pandas as pd
import streamlit as st

def get_model_path():
    possible_paths = [
        os.path.join(os.getcwd(), "models", "predict_flag_invoice.pkl"),
        os.path.join(os.path.dirname(__file__), "..", "models", "predict_flag_invoice.pkl"),
    ]

    for path in possible_paths:
        if os.path.exists(path):
            print(f"Model found at: {path}")
            return path

    raise FileNotFoundError("Model file not found")

def load_model():
    model_path = get_model_path()
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model

model = load_model()
