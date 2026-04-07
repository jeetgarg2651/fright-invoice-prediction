import joblib
import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "predict_freight_model.pkl")

def load_model(model_path: str = MODEL_PATH):
    """
    Load trained freight cost prediction model.
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model


def predict_freight_cost(input_data):
    """
    Predict freight cost for new vendor invoices.

    Parameters
    ----------
    input_data : dict

    Returns
    -------
    pd.DataFrame with predicted freight cost
    """
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Freight'] = model.predict(input_df.values).round()
    return input_df


if __name__ == "__main__":
    # Example inference run (local testing)
    sample_data = {
        "Dollars": [18500, 9000,4000,20000,39999]
    }

    prediction = predict_freight_cost(sample_data)
    print(prediction)
