# Machine learning–based computational drug discovery pipeline for identifying potential inhibitors of soluble epoxide hydrolase (sEH / EPHX2).

Computational drug discovery pipeline for identifying potential inhibitors of **soluble epoxide hydrolase (sEH / EPHX2)** using machine learning, virtual screening, molecular docking, ADMET filtering, and molecular dynamics simulations.

---

## Project Overview

Soluble epoxide hydrolase (sEH), encoded by the **EPHX2 gene**, plays a key role in lipid metabolism and regulation of inflammation, cardiovascular diseases, and pain pathways. Inhibiting sEH has emerged as a promising therapeutic strategy.

This project implements a **multi-stage computational drug discovery pipeline** to identify potential sEH inhibitors using publicly available bioactivity data and structure-based drug design techniques.

The workflow integrates **cheminformatics, machine learning, molecular docking, and molecular dynamics simulations** to prioritize compounds with strong inhibitory potential.

---

## Target Protein

**Protein:** Soluble Epoxide Hydrolase (sEH)  
**Gene:** EPHX2  
**ChEMBL Target ID:** CHEMBL1929  
**Example PDB Structure:** 3ANS  

sEH functions as a homodimeric enzyme responsible for converting epoxides to diols. Inhibiting this enzyme has shown therapeutic potential for:

- Inflammation
- Hypertension
- Cardiovascular disorders
- Neuropathic pain

---

## Computational Pipeline

The project follows a multi-stage computational workflow:

### 1. Data Collection
Bioactivity data for sEH inhibitors was retrieved from **ChEMBL database**.

Dataset includes:

- IC50 values
- SMILES structures
- Compound identifiers

After preprocessing and filtering, a curated dataset was generated for modeling.

---

### 2. Data Preprocessing

Processing steps included:

- Removal of duplicate compounds
- Standardization of IC50 values
- Conversion to **pIC50**
- SMILES validation
- Removal of missing values

Final dataset used for machine learning modeling.

---

### 3. Feature Generation

Molecular descriptors and fingerprints were calculated using **RDKit**.

Features include:

- Molecular weight
- LogP
- Topological polar surface area
- Hydrogen bond donors and acceptors
- Molecular fingerprints (ECFP / Morgan)

These descriptors were used as input features for QSAR modeling.

---

### 4. Machine Learning Model (QSAR)

Multiple regression models were trained to predict **pIC50 values** of compounds.

Models evaluated include:

- Ridge Regression
- Random Forest
- XGBoost
- LightGBM
- CatBoost

Model performance was evaluated using:

- R² Score
- RMSE
- MAE
- Cross-validation

---

### 5. Virtual Screening

The trained model was applied to screen a compound library to identify potential inhibitors with high predicted pIC50 values.

Top candidates were selected for further structure-based evaluation.

---

### 6. Molecular Docking

Selected compounds were docked against the **sEH catalytic binding pocket**.

Docking objectives:

- Predict binding pose
- Estimate binding affinity
- Identify key protein-ligand interactions

Docking results were ranked based on binding scores.

---

### 7. ADMET Filtering

Top compounds were filtered based on predicted pharmacokinetic properties.

Evaluated properties include:

- Lipinski Rule of Five
- Drug-likeness
- Toxicity risk
- Absorption and metabolism predictions

---

### 8. Molecular Dynamics Simulation

Promising protein-ligand complexes were prepared for **molecular dynamics simulations**.

Simulation steps include:

1. System preparation
2. Energy minimization
3. NVT equilibration
4. NPT equilibration
5. Production MD simulation

MD simulations were used to evaluate:

- Complex stability
- RMSD
- RMSF
- Hydrogen bonding
- Binding interactions

---


---

## Tools and Libraries

Python ecosystem:

- RDKit
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- Pandas
- NumPy

Computational chemistry tools:

- AutoDock Vina
- GROMACS
- PyMOL
- VMD

---

## Key Results

- Machine learning models successfully predicted pIC50 values of sEH inhibitors.
- Virtual screening identified potential candidate molecules with strong predicted activity.
- Docking studies suggested favorable binding interactions within the sEH catalytic pocket.
- MD simulations provided insights into protein-ligand stability.

---

## Applications

This pipeline can be adapted for:

- drug discovery
- inhibitor design
- QSAR modeling
- computational chemistry research
- bioinformatics drug target studies

---

## Future Work

Possible extensions include:

- Graph neural network models
- generative AI for molecule design
- free energy calculations
- experimental validation of predicted inhibitors

---

## Author

Bioinformatics and Computational Drug Discovery Project

Focus Areas:

- Bioinformatics
- Machine Learning
- Drug Discovery
- Molecular Modeling

---

## License

This project is intended for academic and research purposes.

## Repository Structure
