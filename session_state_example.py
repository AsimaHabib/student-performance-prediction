
import streamlit as st

# Counter ki initial value sirf pehli baar set hogi
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Button click hone par counter barhega
if st.button("Click me"):
    st.session_state.counter += 1

# Counter ki current value show hogi
st.write("Counter:", st.session_state.counter)
