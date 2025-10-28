# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from watson_mock import call_granite
from src.ai.prompts import disease_prediction_prompt, treatment_plan_prompt
from src.ml.predictor import predict_from_symptoms

# -------------------- PAGE CONFIGURATION --------------------
st.set_page_config(page_title="HealthAI — Intelligent Healthcare Assistant", layout="wide")

# -------------------- CUSTOM CSS DESIGN --------------------
st.markdown("""
    <style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #e0f7fa, #f1f8e9);
        font-family: 'Segoe UI', sans-serif;
        color: black !important;
    }

    /* Titles */
    h1, h2, h3, h4, h5, h6, p, label, div, span {
        color: black !important;
    }

    h1 {
        text-align: center;
        font-size: 3em;
        font-weight: 700;
    }

    h2, h3 {
        font-weight: 600;
    }

    /* Text area, inputs */
    .stTextArea textarea, .stTextInput input, .stSelectbox div, .stNumberInput input {
        border-radius: 10px;
        border: 1px solid #80cbc4;
        background-color: #ffffff;
        color: black !important;
    }

    /* Buttons */
    div.stButton > button:first-child {
        background-color: #00796b;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        transition: 0.3s;
    }

    div.stButton > button:first-child:hover {
        background-color: #004d40;
        transform: scale(1.05);
    }

    /* Subheaders */
    .stSubheader {
        font-weight: 600;
    }

    /* Tab text */
    button[data-baseweb="tab"] > div {
        color: black !important;
        font-weight: 500;
    }

    /* Info boxes and success messages */
    .stAlert {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown("<h1>💙 HealthAI — Intelligent Healthcare Assistant 🩺</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Empowering your health with AI — Personalized insights, smart predictions & visual analytics.</p>", unsafe_allow_html=True)
st.write("---")

# -------------------- TABS --------------------
tabs = st.tabs(["💬 Patient Chat", "🧠 Disease Prediction", "💊 Treatment Plans", "📊 Health Analytics"])

# -------------------- PATIENT CHAT --------------------
with tabs[0]:
    st.header("💬 Patient Chat")
    st.write("Ask your health-related questions and get intelligent responses powered by AI simulation.")

    user_q = st.text_area("💭 Type your question here:")
    if st.button("Ask AI 🤖"):
        with st.spinner("Thinking..."):
            prompt = f"You are a helpful healthcare assistant. Be concise but informative. Question: {user_q}"
            resp = call_granite(prompt)
        st.success("✅ Response received:")
        st.markdown(f"<div style='background-color:#f0fdf4;padding:15px;border-radius:10px;color:black;'>{resp}</div>", unsafe_allow_html=True)

# -------------------- DISEASE PREDICTION --------------------
with tabs[1]:
    st.header("🧠 Disease Prediction")
    st.write("Describe your symptoms below to get likely conditions and AI-based recommendations.")
    
    symptoms = st.text_area("🩺 Enter your symptoms:")
    age = st.slider("🎂 Age", 1, 100, 25)
    sex = st.selectbox("⚧️ Sex", ["Female", "Male", "Other"])

    if st.button("Predict Disease 🔍"):
        with st.spinner("Analyzing symptoms..."):
            preds = predict_from_symptoms(symptoms)
            st.subheader("📋 Possible Conditions:")
            for p, prob in preds:
                st.write(f"- {p} — **{prob*100:.1f}% likelihood**")

            # AI explanation
            prompt = disease_prediction_prompt(symptoms, {"age": age, "sex": sex})
            explain = call_granite(prompt)

        st.subheader("🧩 AI Insights & Recommendations")
        st.markdown(f"<div style='background-color:#fff3e0;padding:15px;border-radius:10px;color:black;'>{explain}</div>", unsafe_allow_html=True)

# -------------------- TREATMENT PLANS --------------------
with tabs[2]:
    st.header("💊 Personalized Treatment Plan")
    st.write("Generate an evidence-based treatment suggestion for your condition.")

    diagnosis = st.text_input("📋 Enter diagnosis or condition:")
    constraints = st.text_area("⚠️ Enter patient constraints (allergies, pregnancy, etc.):")

    if st.button("Generate Plan 🩹"):
        with st.spinner("Generating treatment recommendations..."):
            prompt = treatment_plan_prompt(diagnosis, {"age": age, "sex": sex}, constraints)
            plan = call_granite(prompt)

        st.subheader("🩵 Suggested Treatment Plan")
        st.markdown(f"<div style='background-color:#e3f2fd;padding:15px;border-radius:10px;color:black;'>{plan}</div>", unsafe_allow_html=True)

# -------------------- HEALTH ANALYTICS --------------------
with tabs[3]:
    st.header("📊 Health Analytics Dashboard")
    st.write("Use the sliders below to input your health metrics and visualize trends instantly.")

    # Input vitals
    st.subheader("🩸 Input Your Latest Health Metrics:")
    heart_rate = st.slider("❤️ Heart Rate (bpm)", 50, 150, 80)
    bp_sys = st.slider("💓 Blood Pressure — Systolic (mmHg)", 90, 180, 120)
    bp_dia = st.slider("💓 Blood Pressure — Diastolic (mmHg)", 60, 120, 80)
    glucose = st.slider("🩷 Blood Glucose (mg/dL)", 70, 250, 100)
    oxygen = st.slider("🫁 SpO₂ (%)", 85, 100, 98)

    # Simulate past 7 readings (for plotting)
    import numpy as np
    import datetime
    dates = [datetime.date.today() - datetime.timedelta(days=i) for i in range(6, -1, -1)]
    df = pd.DataFrame({
        "Date": dates,
        "Heart Rate": np.random.normal(heart_rate, 5, 7).astype(int),
        "Systolic BP": np.random.normal(bp_sys, 5, 7).astype(int),
        "Diastolic BP": np.random.normal(bp_dia, 3, 7).astype(int),
        "Glucose": np.random.normal(glucose, 8, 7).astype(int),
        "SpO2": np.random.normal(oxygen, 1, 7).astype(int)
    })

    st.subheader("📈 Health Metrics Over the Week")
    fig = px.line(df, x="Date", y=["Heart Rate", "Systolic BP", "Diastolic BP", "Glucose", "SpO2"],
                  markers=True, line_shape="spline",
                  color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(title="🩺 Your Weekly Health Trends", xaxis_title="Date", yaxis_title="Measurement Value",
                      plot_bgcolor="#ffffff", paper_bgcolor="#ffffff", font=dict(color="black"))

    st.plotly_chart(fig, use_container_width=True)

    st.info("💡 Tip: Adjust the sliders to simulate different health readings and observe the graph update dynamically!")
