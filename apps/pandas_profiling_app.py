import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import streamlit as st

st.header("Streamlit Pandas Profiling")

df = pd.read_csv(
    "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"
)

report = df.profile_report()

st_profile_report(report)
