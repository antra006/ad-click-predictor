import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    h1 {
        text-align: center;
        color: #00FFD1;
        font-size: 50px;
    }
    .stButton>button {
        background-color: #00FFD1;
        color: black;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)


# Title
st.markdown("<h1> Ad Click Predictor</h1>", unsafe_allow_html=True)
st.write("### Predict whether a user will click on an ad ")

# Input fields
time_spent = st.slider("Time on Site (minutes)", 0, 100, 60)
age = st.slider("Age (yrs)", 18, 60, 25)
income = st.slider("Income (₹)", 10000, 100000, 50000)
internet_usage = st.slider("Internet Usage (MB)", 50, 500, 200)
# Load data
data = pd.read_csv("advertising.csv")

# Prepare model
X = data[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage']]
y = data['Clicked on Ad']

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Predict
if st.button("Predict "):
    prediction = model.predict([[time_spent, age, income, internet_usage]])
    prob = model.predict_proba([[time_spent, age, income, internet_usage]])

    confidence = prob[0][prediction[0]] * 100

    if prediction[0] == 1:
        st.success(" User WILL click the ad")
    else:
        st.error(" User will NOT click the ad")

    st.write(f"Confidence: {confidence:.2f}%")
