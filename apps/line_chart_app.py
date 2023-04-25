import numpy as np
import pandas as pd
import streamlit as st

st.header("Line chart")

df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(df)
