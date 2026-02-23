import streamlit as st
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Milk Quality Prediction", page_icon="🥛")

st.title("🥛 Milk Quality Prediction using XGBoost")

# ---------------------------
# Sample Milk Dataset
# ---------------------------
data = {
    "pH": [6.6, 6.8, 6.4, 6.7, 6.5, 6.9, 6.3, 6.8],
    "Temperature": [38, 40, 42, 39, 37, 41, 43, 38],
    "Taste": [1, 1, 0, 1, 0, 1, 0, 1],
    "Odor": [1, 1, 0, 1, 0, 1, 0, 1],
    "Fat": [1, 1, 0, 1, 0, 1, 0, 1],
    "Turbidity": [1, 1, 0, 1, 0, 1, 0, 1],
    "Colour": [255, 250, 240, 255, 245, 250, 235, 255],
    "Grade": ["High", "High", "Low", "High", "Low", "High", "Low", "High"]
}

df = pd.DataFrame(data)

# Encode target
le = LabelEncoder()
df["Grade"] = le.fit_transform(df["Grade"])

X = df.drop("Grade", axis=1)
y = df["Grade"]

# Train model
model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
model.fit(X, y)

# ---------------------------
# User Input
# ---------------------------
st.subheader("Enter Milk Parameters")

ph = st.number_input("pH Level", 6.0, 7.5, 6.7)
temp = st.number_input("Temperature (°C)", 30, 50, 38)
taste = st.selectbox("Taste", [0, 1])
odor = st.selectbox("Odor", [0, 1])
fat = st.selectbox("Fat", [0, 1])
turbidity = st.selectbox("Turbidity", [0, 1])
colour = st.number_input("Colour", 200, 255, 255)

# Prediction
if st.button("Predict Milk Quality"):
    input_data = pd.DataFrame([[ph, temp, taste, odor, fat, turbidity, colour]],
                              columns=X.columns)
    
    prediction = model.predict(input_data)[0]
    result = le.inverse_transform([prediction])[0]
    
    if result == "High":
        st.success("🥛 Milk Quality: HIGH")
    else:
        st.error("⚠️ Milk Quality: LOW")