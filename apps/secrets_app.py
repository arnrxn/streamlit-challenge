import streamlit as st

st.title("Secrets")

st.write(f'{st.secrets["MESSAGE"]} {st.secrets["my_cool_secrets"]["USERNAME"]}!')
