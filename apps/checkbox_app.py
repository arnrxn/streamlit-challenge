import streamlit as st

st.header("Checkbox")

st.write("What would you like to order?")

icecream = st.checkbox("Ice cream")
coffee = st.checkbox("coffee")
cola = st.checkbox("cola")

if icecream:
    st.write("Great! Here's some 🍦")

if coffee:
    st.write("Okay, here's some ☕")

if cola:
    st.write("Here you go 🥤")
