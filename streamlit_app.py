import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.set_page_config(
    page_title="Student Predictor",
    page_icon="🎓",
    layout="centered",
)


# ---------- Header ----------
st.title("🎓 Student Pass / Fail Predictor")
st.markdown("Enter Student details and predict result.")
st.divider()

# ---------- Inputs ----------
st.subheader("📚 Student Information")

col1, col2 = st.columns(2)

with col1:
    study_hours = st.slider(
        "Daily Study Hours",
        min_value=0.0,
        max_value=12.0,
        value=4.0,
        step=0.5,
        help="Student roz kitne ghante parhta hai",
    )

with col2:
    prev_score = st.slider(
        "Previous Score",
        min_value=0,
        max_value=100,
        value=60,
        step=1,
        help="Pichle exam ka score (0-100)",
    )

# Selected values ko metrics mein dikhayein
m1, m2 = st.columns(2)
m1.metric("Study Hours", f"{study_hours} hrs")
m2.metric("Previous Score", f"{prev_score}%")

st.divider()


# ---------- Prediction ----------
def get_prediction(hours: float, score: int) -> dict:
    response = requests.post(
        f"{API_URL}/predict",
        json={"study_hours": hours, "prev_score": score},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


if st.button("🔍 Predict Student Result", type="primary", use_container_width=True):
    try:
        with st.spinner("Prediction ho rahi hai..."):
            result = get_prediction(study_hours, prev_score)

        st.success("Prediction completed!")

        # Result ko readable format mein dikhayein
        prediction = str(result.get("prediction", result.get("result", ""))).lower()

        if prediction in ("pass", "1", "true"):
            st.balloons()
            st.markdown("### ✅ Result: **PASS**")
        elif prediction in ("fail", "0", "false"):
            st.markdown("### ❌ Result: **FAIL**")
        else:
            st.markdown(f"### Result: **{prediction or 'Unknown'}**")

        # Agar API probability bhejti hai to dikhayein
        probability = result.get("probability")
        if probability is not None:
            st.progress(float(probability), text=f"Confidence: {float(probability):.0%}")

        with st.expander("🔧 Raw API response"):
            st.json(result)

    except requests.exceptions.ConnectionError:
        st.error("FastAPI server chal nahi raha! Pehle FastAPI start karein.")
    except requests.exceptions.Timeout:
        st.error("Server ne time par jawab nahi diya. Dobara try karein.")
    except requests.exceptions.HTTPError as e:
        st.error(f"API Error: {e.response.text}")
    except ValueError:
        st.error("API se invalid response mila.")