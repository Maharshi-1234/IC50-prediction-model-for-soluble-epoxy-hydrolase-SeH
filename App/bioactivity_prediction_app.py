import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import numpy as np
import base64
from PIL import Image

# ================= CONFIG =================
BASE_DIR = Path(__file__).parent

MODEL_PATH = BASE_DIR / "seh_model_XGBoost_20260130_051249.pkl"
SCALER_PATH = BASE_DIR / "seh_scaler.pkl"
FEATURE_LIST_PATH = BASE_DIR / "seh_features_20260130_051249.txt"
LOGO_PATH = BASE_DIR / "logo.png"
# ==========================================


def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'


def predict_activity(descriptor_df, molecule_names):

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)


    X_scaled = scaler.transform(descriptor_df.values)
    predictions = model.predict(X_scaled)

    out = pd.DataFrame({
        "Molecule": molecule_names,
        "Predicted_pIC50": predictions
    })

    st.subheader("Prediction Results")
    st.write(out)
    st.markdown(filedownload(out), unsafe_allow_html=True)


# ================= UI =================
if LOGO_PATH.exists():
    st.image(Image.open(LOGO_PATH), use_container_width=True)

st.title("Web-Based QSAR Bioactivity Prediction for sEH")
st.markdown(
    "This web app predicts **pIC50 values of soluble epoxide hydrolase (sEH) inhibitors** "
    "using a trained XGBoost QSAR model."
)

with st.sidebar:
    st.header("Upload Descriptor File")
    uploaded_file = st.file_uploader(
    "Upload Descriptor File",
    type=["csv", "txt"]
)

    predict_button = st.button("Predict")

# ================= MAIN =================
if predict_button:

    if uploaded_file is None:
        st.error("Please upload a descriptor CSV file.")
        st.stop()

    desc = pd.read_csv(uploaded_file)

    with open(FEATURE_LIST_PATH) as f:
        selected_features = [line.strip() for line in f if line.strip()]

    desc = desc.reindex(columns=selected_features, fill_value=0)

    molecule_names = [f"Molecule_{i+1}" for i in range(len(desc))]

    predict_activity(desc, molecule_names)

else:
    st.info("Upload descriptor CSV and click Predict.")
