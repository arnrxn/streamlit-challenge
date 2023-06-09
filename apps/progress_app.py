import time
import streamlit as st

st.title("Progress bar")

with st.expander("About this app"):
    st.write(
        "You can now display the progress of your calculations in a Streamlit app with the `st.progress` command."
    )

progress_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.05)
    progress_bar.progress(percent_complete + 1)

st.balloons()
