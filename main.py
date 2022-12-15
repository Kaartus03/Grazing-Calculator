import streamlit as st
from PIL import Image
st.title("Holistic Grazing Area Calculator")
img = Image.open("graze.jpg")
st.image(img)

# Introduction
st.subheader("What is Holistic Grazing?")
st.text("Under rotational grazing, only one portion of pasture is grazed at a time while the 
        "remainder of the pasture" "“rests. Pastures are subdivided into smaller areas"
        "(referred to as paddocks)"" and livestock are moved from one paddock to another. Resting"
        "grazed paddocks allows forage plants to renew energy reserves,"" rebuild vigor, deepen" 
        "their root system, and give ""long-term maximum production.Rotational grazing can be" 
        "practiced in a variety of intensities."" Systems can range from 2 to 30 or more paddocks."
        " Management intensive rotational grazing ""involves a higher level of management with greater"
        "paddock numbers, shorter grazing periods, ""and longer rest periods. Generally, more intense"
        "management results in greater livestock production ""per acre.We have developed calculator"
        "that calculates the total grazing area required."
        " This tool has two assumptions "
        "1-Dry feed is about 60% of the fresh green grass."
        "2-40% of the total yield will be protected for regeneration. "
        "Formula Used is "
        "𝐴𝑟𝑒𝑎=(W 𝑥 𝐶)/(0.36 𝑥 𝐺) "
        "Where, "
        " W= Percentage of Body Weight of animal."
        " A = Total Area Required for grazing "
        "C = Animal Units (1 Unit = 720 kg ≈ 1 Cow or 7 Sheeps) "
        "G = Grass yield per Day")

# Input Values
weight = st.number_input("Enter Percentage Body Weight of Animal Unit in KG", step=1)
C = st.number_input("Enter the Total Number of Animal Units", step=1)
G = st.number_input("Enter the Grass Yield per Day", step=0.1)
Area = (weight*C)/(0.36*G)

st.success(f"Total area Required is {Area}")
