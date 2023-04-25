import streamlit as st

st.header("Selectbox")

option = st.selectbox("What is your favourite color?", ("Blue", "Green", "Red"))

st.write("Your favorite color is ", option)
