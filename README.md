# 🚀 Vendor Invoice Intelligence System

An end-to-end Machine Learning system designed to help finance teams **predict freight costs** and **detect high-risk invoices**.

---

## 📌 Table of Contents

* [📖 Project Overview](#-project-overview)
* [🎯 Business Objective](#-business-objective)
* [🗄️ Data Source](#️-data-source)
* [📊 Exploratory Data Analysis (EDA)](#-exploratory-data-analysis-eda)
* [🤖 Models Used](#-models-used)
* [📈 Evaluation Metrics](#-evaluation-metrics)
* [💻 Application](#-application)
* [📁 Project Structure](#-project-structure)
* [▶️ How to Run This Project](#️-how-to-run-this-project)
* [👨‍💻 Author](#-author)

---

## 📖 Project Overview

This project implements an end-to-end Machine Learning pipeline designed to support finance teams by:

* Predicting expected freight costs for vendor invoices
* Flagging high-risk invoices that require manual review

The system helps detect abnormal cost, freight, and operational patterns.

---

## 🎯 Business Objective

* Reduce **financial leakage**
* Improve **cost forecasting**
* Automate **invoice validation process**
* Enable **real-time decision making**

---

## 🗄️ Data Source

Data is stored locally (or during training phase) and processed into ML-ready format.

Typical features include:

* Invoice quantity
* Invoice amount
* Freight cost
* Total item quantity
* Total item dollars

---

## 📊 Exploratory Data Analysis (EDA)

* Checked relationship between **freight and invoice value**
* Identified **anomalous invoices**
* Compared flagged vs normal invoices
* Analyzed distribution of costs and quantities
* 

---

## 🤖 Models Used

### 🔹 Freight Cost Prediction (Regression)

* Linear Regression
* Decision Tree Regressor
* ✅ Random Forest Regressor (Final Model)
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/da50af18-fac0-4de6-989d-1ecebbfed595" />

---

### 🔹 Invoice Risk Detection (Classification)

* Logistic Regression
* Decision Tree Classifier
* ✅ Random Forest Classifier (Final Model)

---

## 📈 Evaluation Metrics

### Regression

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

### Classification

* Accuracy
* Precision
* Recall
* F1-score

---

## 💻 Application

A Streamlit-based web app that allows users to:

* Input invoice details
* Predict freight cost instantly
* Detect risky invoices
* View results in real-time



---

## 📁 Project Structure

```
project/
│
├── app/
│   └── webapp.py              # Streamlit app
│
├── inference/
│   ├── predict_freight.py     # Freight prediction logic
│   └── predict_invoice.py     # Invoice risk logic
│
├── models/
│   ├── predict_freight_model.pkl
│   └── predict_flag_invoice.pkl
│
├── freight_cost_prediction/   # Training (regression)
├── invoice_flagging/          # Training (classification)
├── notebooks/                 # EDA & experiments
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run This Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2️⃣ Setup Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

---

### 3️⃣ Run Application

```bash
streamlit run app/webapp.py
```

---

## ⚠️ Important Notes

* Use **relative paths only** (no `D:\` paths)
* Ensure `.pkl` models exist in `models/`
* Do not upload large datasets
* Fix imports using `__init__.py` if needed

---

## 👨‍💻 Author

NAME - JEET GARG
LINKDIN ID - https://www.linkedin.com/in/jeet-garg-49b9a2290?utm_source=share_via&utm_content=profile&utm_medium=member_ios

Built to make invoice processing **smarter, faster, and more reliable** using Machine Learning.

---

⭐ If you like this project, give it a star!
