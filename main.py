import streamlit as st
from PIL import Image
st.title("Holistic Grazing Area Calculator")
img = Image.open("graze.jpg")
st.image(img)

# Introduction
st.subheader("Formula")
st.text(
        "𝐴𝑟𝑒𝑎=(W 𝑥 𝐶)/(0.36 𝑥 𝐺) "
        "Where, "
        " W= Percentage of Body Weight consumption of animal (kg)."
        " A = Total Area Required for grazing (Acres) "
        "C = Animal Units in Nos. (1 Unit = 720 kg ≈ 1 Cow or 7 Sheeps) "
        "G = Grass yield (Dry Feed in kg/acres)")

# Input Values
weight = st.number_input("Enter Percentage Body Weight of Animal Unit in KG", step=1)
C = st.number_input("Enter the Total Number of Animal Units in No.", step=1)
G = st.number_input("Enter the Grass Yield per Day (kg/d)", step=0.1)
Area = (weight*C)/(0.36*G)

st.success(f"Total area Required is {Area}")
