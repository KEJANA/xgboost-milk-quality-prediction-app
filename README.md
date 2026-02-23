# 🥛 Milk Quality Prediction using XGBoost

An end-to-end Machine Learning web application that predicts the quality of milk based on its physicochemical properties using the powerful XGBoost algorithm. This interactive app is built with Streamlit and enables real-time prediction through a user-friendly interface.

---

## 🚀 Project Overview
This project uses the XGBoost (Extreme Gradient Boosting) algorithm to classify milk quality into different categories based on input features such as pH, temperature, taste, odor, fat content, turbidity, and color.

The application is deployed as a Streamlit web app where users can input milk parameters and instantly get the predicted quality level.

---

## 🎯 Objective
- Predict milk quality using supervised machine learning
- Provide real-time predictions through a web interface
- Demonstrate practical implementation of XGBoost in a classification task

---

## 🧠 Algorithm Used
- XGBoost Classifier (Extreme Gradient Boosting)

XGBoost is an optimized gradient boosting algorithm known for its high performance, speed, and accuracy in classification problems.

---

## 📊 Features
- Interactive Streamlit UI
- Real-time prediction
- Efficient XGBoost model
- Clean and user-friendly design
- End-to-end ML workflow (training → deployment)

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

---

## 📂 Project Structure
xgboost-milk-quality-prediction-app/
│── app.py                # Streamlit web application
│── model.pkl             # Trained XGBoost model
│── requirements.txt      # Required Python libraries
│── README.md             # Project documentation
---

## 👩‍💻 Author
**Kejana V**  
AI & Data Science Engineer | Machine Learning & Streamlit Developer

## ▶️ How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
