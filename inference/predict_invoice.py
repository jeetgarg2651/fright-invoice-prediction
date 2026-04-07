import joblib
import pandas as pd

MODEL_PATH = "models/predict_flag_invoice.pkl"

def load_model(model_path: str = MODEL_PATH):
    """
    Load trained invoice flagging model.
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model


def predict_invoice_flag(input_data: dict):
    """
    Predict invoice flag using 5 features.
    """
    model = load_model()

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

    prediction = predict_invoice_flag(sample_data)
    print(prediction)
