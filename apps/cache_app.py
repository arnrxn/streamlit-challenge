import numpy as np
import pandas as pd
import streamlit as st
from time import time

st.title("Cache")

col1, col2 = st.columns(2)

with col1:
    # Using cache
    st.subheader("Using cache")

    N = 4500000

    @st.cache_data
    def load_data_a():
        df = pd.DataFrame(np.random.rand(N, 5), columns=["a", "b", "c", "d", "e"])
        return df

    a0 = time()
    st.write("Load data the first time with cache", load_data_a())
    a1 = time()
    st.write("Load data the second time with cache", load_data_a())
    a2 = time()

    # Not using cache
    st.subheader("**NOT** Using cache")

    def load_data_b():
        df = pd.DataFrame(np.random.rand(N, 5), columns=["a", "b", "c", "d", "e"])
        return df

    b0 = time()
    st.write("Load data the first time without cache", load_data_b())
    b1 = time()
    st.write("Load data the second time without cache", load_data_b())
    b2 = time()

    # Print results
    st.info(f"Seconds elapsed loading data the first time with cache {a1-a0:.2f}")
    st.info(f"Seconds elapsed loading data the first time with cache {a2-a1:.2f}")
    st.info(
        f"Seconds elapsed loading data the first time **without** cache {b1-b0:.2f}"
    )
    st.info(
        f"Seconds elapsed loading data the first time **without** cache {b2-b1:.2f}"
    )


with col2:
    data_url = "https://raw.githubusercontent.com/plotly/datasets/master/26k-consumer-complaints.csv"

    st.subheader("Another example")

    def load_data(url):
        df = pd.read_csv(url)
        return df

    a0 = time()
    df = load_data(data_url)
    st.dataframe(df)
    a1 = time()

    st.info(f"Seconds elapsed without caching: {a1 - a0:.2f}")

    @st.cache_data  # 👈 Add the caching decorator
    def load_data_cached(url):
        df = pd.read_csv(url)
        return df

    b0 = time()
    df = load_data_cached(data_url)
    st.dataframe(df)
    b1 = time()

    st.info(f"Seconds elapsed with caching: {b1 - b0:.2f}")

    st.button("Rerun")
