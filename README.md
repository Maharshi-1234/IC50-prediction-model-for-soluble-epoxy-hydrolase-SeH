
# Web-Based QSAR Modeling for Bioactivity Prediction of Soluble Epoxide Hydrolase (sEH) Inhibitors

## 📌 Project Overview

This project presents an **end-to-end QSAR pipeline** for predicting the bioactivity of **soluble epoxide hydrolase (sEH) inhibitors** using machine learning.
The workflow includes **dataset curation, molecular descriptor generation, model training and validation, interpretability analysis, and deployment as a Streamlit web application**.

The developed model enables **fast and cost-effective virtual screening** of chemical compounds based on SMILES input.

---

## 🎯 Objectives

* Compile a high-quality dataset of sEH inhibitors from **ChEMBL**
* Generate comprehensive molecular descriptors using **PaDEL-Descriptor**
* Train and compare multiple machine learning models
* Perform rigorous validation and interpretability analysis
* Deploy the best-performing model as a **web application**

---

## 🧪 Dataset

* **Target:** Soluble Epoxide Hydrolase (sEH)
* **Source:** ChEMBL database
* **Total compounds:** ~2,500
* **Response variable:** IC₅₀ converted to **pIC₅₀**
* **Data preprocessing:**

  * Duplicate removal
  * Missing value handling
  * Standardization of features

---

## 🧬 Molecular Descriptors

* Tool used: **PaDEL-Descriptor**
* Number of descriptors: **~2,200**
* Descriptor categories:

  * Physicochemical
  * Topological
  * Constitutional
  * Fingerprints

Descriptors were scaled using **StandardScaler**, saved as:

* `seh_features_*.txt`
* `seh_scaler.pkl`

---

## 🤖 Machine Learning Models

Multiple algorithms were evaluated, including:

* Linear Models (Ridge, Lasso, ElasticNet)
* Support Vector Regression
* Random Forest
* Gradient Boosting
* LightGBM
* CatBoost
* **XGBoost (Best Model)**

### ⭐ Best Model Performance

* **Model:** XGBoost Regressor
* **R²:** ~0.82
* **Validation:**

  * Train/Test split
  * Cross-validation
  * Y-randomization
  * Applicability domain analysis

Saved model files:

* `seh_model.pkl`
* `seh_scaler.pkl`

---

## 🔍 Model Interpretability

* **SHAP (SHapley Additive exPlanations)** was used
* Key influential descriptors:

  * LogP
  * Molecular weight
  * Hydrogen bond acceptors
  * Aromatic ring count
  * TPSA

---

## 🌐 Web Application (Streamlit)

The trained model is deployed as a **Streamlit web app** that allows users to:

* Input SMILES strings
* Generate molecular descriptors
* Predict bioactivity (pIC₅₀)
* Download prediction results

---

## ▶️ How to Run the Project Locally

### 1️⃣ Create a virtual environment

```bash
conda create -n seh_qsar python=3.8
conda activate seh_qsar
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Launch the Streamlit app

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
seh_qsar_project/
│
├── App/                # Streamlit application
├── Models/             # Trained models & scaler
├── Descriptors/        # PaDEL descriptor outputs
├── Notebooks/          # Jupyter notebooks
├── Results/            # Prediction results
├── Notes_and_PPT/      # Project presentation
├── requirements.txt
└── README.md
```

---

## 🚀 Conclusion

This project demonstrates the successful application of **machine learning-based QSAR modeling** for predicting sEH inhibitor potency.
The developed pipeline is **robust, interpretable, and deployment-ready**, enabling efficient virtual screening in early-stage drug discovery.

---

## 👤 Author

**M. Ramana Maharshi**
B.Tech Bioinformatics

---