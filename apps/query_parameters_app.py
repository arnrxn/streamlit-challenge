import streamlit as st

st.title("Experimental get query parameters")

with st.expander("About this app"):
    st.write(
        "`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser."
    )

# Instructions
st.markdown(
    """
        In the above URL bar of your internet browser, append the following:
        `?firstname=Jack&surname=Beanstalk`
        after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
        such that it becomes 
        `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
    """
)

query_params = st.experimental_get_query_params()

# Contents of st.experimental_get_query_params
st.header("Contents of st.experimental_get_query_params")
st.write(query_params)

# Retrieving and displaying information from the URL
st.header("Retrieving and displaying information from the URL")

firstname = query_params["firstname"][0]
surname = query_params["surname"][0]

st.write(f"Hello **{firstname} {surname}**, how are you?")
