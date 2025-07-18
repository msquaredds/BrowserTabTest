import time

import streamlit as st

st.title("Spinner Test Page")

with st.spinner():
    time.sleep(3)
