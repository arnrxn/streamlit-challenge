import pandas as pd
import streamlit as st

st.title("File uploader")

st.subheader("Input CSV")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("DataFrame")
    st.write(df)

    st.subheader("Descriptive Statistics")
    st.write(df.describe())
else:
    st.info("☝️ Upload a CSV file")
