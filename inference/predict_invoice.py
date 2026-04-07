import os
import joblib

# Update model path to relative
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models", "predict_freight_model.pkl")
model = joblib.load(model_path)

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
