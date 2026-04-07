import joblib
import pandas as pd
import os

def get_model_path():
    # Try multiple possible paths (safe for deployment)
    possible_paths = [
        os.path.join(os.getcwd(), "models", "predict_freight_model.pkl"),
        os.path.join(os.path.dirname(__file__), "..", "models", "predict_freight_model.pkl"),
    ]

    for path in possible_paths:
        if os.path.exists(path):
            print(f"Model found at: {path}")
            return path

    raise FileNotFoundError("Model file not found in expected locations.")

def load_model():
    model_path = get_model_path()
    with open(model_path, "rb") as f:
        model = joblib.load(f)
    return model


def predict_freight_cost(input_data):
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Freight'] = model.predict(input_df.values).round()
    return input_df


if __name__ == "__main__":
    sample_data = {
        "Dollars": [18500, 9000, 4000, 20000, 39999]
    }

    prediction = predict_freight_cost(sample_data)
    print(prediction)
