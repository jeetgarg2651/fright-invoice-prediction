import os
import joblib
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "predict_freight_model.pkl")  # Adjust filename if needed

def load_model(model_path: str = MODEL_PATH):
    """
    Load trained invoice flag prediction model.
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model

model = load_model()

def predict_freight(input_data: dict):
    """
    Predict freight using 5 features.
    """
    # Convert to DataFrame
    input_df = pd.DataFrame(input_data)

    # REQUIRED FEATURES
    required_cols = [
        "invoice_quantity",
        "invoice_dollars",
        "Freight",
        "total_item_quantity",
        "total_item_dollars"
    ]

    # Correct variable name
    input_df = input_df[required_cols]

    # Prediction
    input_df["Predicted_Flag"] = model.predict(input_df)

    return input_df


if __name__ == "__main__":
    sample_data = {
        "invoice_quantity": [10, 20, 90],
        "invoice_dollars": [1000, 5000, 1000],
        "Freight": [100, 300, 400],
        "total_item_quantity": [10, 18, 80],
        "total_item_dollars": [950, 4800, 8000]
    }

    prediction = predict_freight(sample_data)
    print(prediction)
