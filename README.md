# 💳 Fraud Detection System

A machine learning-based web application that detects fraudulent financial transactions in real time. Built using classification models and deployed with an interactive interface.
Link : https://fraud-detection-1-7qeu.onrender.com

---

## 🚀 Overview

Financial fraud is a major issue in digital transactions. This project uses machine learning to identify suspicious transactions based on patterns in transaction data such as amount, balance changes, and transaction type.

---

## 🧠 Features

* Detects fraudulent vs non-fraudulent transactions
* Uses machine learning models (XGBoost / Logistic Regression)
* Data preprocessing with pipelines
* Interactive web interface (Streamlit)
* Handles class imbalance
* Feature importance analysis

---

## 📊 Dataset 
link : https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download

The dataset contains the records of financial transactions for fraud detection. (6.3 Million Records)
Some of these records were flagged false by existing algorithms.

Further approaches could be used to feature engineer properties that could further strengthen the fraud detection algorithms as well as find out where the existing algorithm lacks.

CASH-IN: is the process of increasing the balance of
account by paying in cash to a merchant.

CASH-OUT: is the opposite process of CASH-IN, it
means to withdraw cash from a merchant which decreases
the balance of the account.

DEBIT: is similar process than CASH-OUT and involves sending the money from the mobile money service
to a bank account.

PAYMENT: is the process of paying for goods or services to merchants which decreases the balance of the account and increases the balance of the receiver.

TRANSFER: is the process of sending money to another user of the service through the mobile money platform
