
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Student Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Pass / Fail Predictor")
st.markdown("Enter the student's details below to predict their result.")
st.markdown("---")



st.subheader("📚 Student Information")

col1, col2 = st.columns(2)

with col1:
    study_hours = st.slider(
        "Daily Study Hours",
        min_value=0.0,
        max_value=12.0,
        value=4.0,
        step=0.5
    )

with col2:
    prev_score = st.slider(
        "Previous Score",
        min_value=0,
        max_value=100,
        value=60,
        step=1
    )

st.write("Study Hours:", study_hours)
st.write("Previous Score:", prev_score)



if st.button("🔍 Predict Student Result"):
    try:
        response = requests.post(
            f"{API_URL}/predict",
            json={
                "study_hours": study_hours,
                "prev_score": prev_score
            }
        )

        if response.status_code == 200:
            result = response.json()
            st.success("Prediction completed!")
            st.json(result)
        else:
            st.error(f"API Error: {response.text}")

    except requests.exceptions.ConnectionError:
        st.error(
            "FastAPI server is not running! "
            "Please start FastAPI first."
        )
