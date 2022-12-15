import streamlit as st
from PIL import Image
st.title("Holistic Grazing Area Calculator")
img = Image.open("graze.jpg")
st.image(img)

# Introduction
st.subheader("What is Holistic Grazing?")
st.text("Here We need to write smething guys just to look cool")

# Input Values
weight = st.number_input("Enter Percentage Body Weight of Animal Unit in KG", step=1)
C = st.number_input("Enter the Total Number of Animal Units", step=1)
G = st.number_input("Enter the Grass Yield per Day", step=0.1)
Area = (weight*C)/(0.36*G)

st.success(f"Total area Required is {Area}")
