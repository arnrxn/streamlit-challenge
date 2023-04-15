import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


st.header("st.write")

# Example 1
st.write("Hello, *World!* :sunglasses:")

# Example 2
st.write(1234)

# Example 3
df = pd.DataFrame(
    {
        "first": [1, 3, 4, 5],
        "second": [10, 30, 40, 50],
    }
)
st.write(df)

# Example 4
st.write("Below is a df:", df, "Above is a df")

# Example 5
df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
chart = (
    alt.Chart(df2)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.write(chart)
