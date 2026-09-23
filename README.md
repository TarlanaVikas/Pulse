# Pulse - Multiple Disease Prediction System

<div align="center">

**ML-powered web application for predicting Diabetes, Heart Disease, and Parkinson's Disease.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge\&logo=scikit-learn\&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)](https://pandas.pydata.org/)
[![GitHub](https://img.shields.io/badge/GitHub-TarlanaVikas-181717?style=for-the-badge\&logo=github)](https://github.com/TarlanaVikas/Pulse)

</div>

---

## Overview

**Pulse** is a Streamlit-based machine learning application that predicts the likelihood of:

* Diabetes
* Heart Disease
* Parkinson's Disease

It uses pre-trained machine learning models and provides an interactive interface for entering patient-related parameters and viewing predictions.

> **Disclaimer:** For educational purposes only. Predictions are not medical diagnoses or medical advice.

---

## Features

* Multiple disease prediction
* Interactive Streamlit UI
* Pre-trained ML models
* Dataset-based model development
* Simple and lightweight interface

---

## Tech Stack

**Python · Streamlit · Scikit-learn · Pandas · NumPy · Pickle · Jupyter Notebook**

---

## Project Structure

```text
Pulse/
├── multiplediseaseprediction.py
├── diabetes_model.sav
├── heart_disease_model.sav
├── parkinsons_model.sav
├── diabetes.csv
├── heart.csv
├── parkinsons.csv
├── Multiple Disease Prediction System - Diabetes.ipynb
├── Multiple Disease Prediction System - Heart.ipynb
├── Multiple Disease Prediction System - Parkinsons.ipynb
├── requirements.txt
└── README.md
```

---

## Run Locally

```bash
git clone https://github.com/TarlanaVikas/Pulse.git
cd Pulse
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run multiplediseaseprediction.py
```

Open:

```text
http://localhost:8501
```

---

## Deploy

The application can be deployed using **Streamlit Community Cloud**.

Set:

```text
Repository: TarlanaVikas/Pulse
Branch: main
Main file: multiplediseaseprediction.py
```

Then deploy.

---

## Author

**Vikas Tarlana**

[![GitHub](https://img.shields.io/badge/GitHub-TarlanaVikas-181717?style=flat-square\&logo=github)](https://github.com/TarlanaVikas)

