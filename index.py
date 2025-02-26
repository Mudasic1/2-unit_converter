import streamlit as st

# Length conversion factors
conversion_factors = {
    "Meter": 1,
    "Kilometer": 0.001,
    "Centimeter": 100,
    "Millimeter": 1000,
    "Mile": 0.000621371,
    "Yard": 1.09361,
    "Foot": 3.28084,
    "Inch": 39.3701
}

st.title("Length Converter")

# User input for length
value = st.number_input("Enter value:", min_value=0.0, value=1.0, step=0.1)

# Dropdowns for selecting units
from_unit = st.selectbox("From Unit:", conversion_factors.keys())
to_unit = st.selectbox("To Unit:", conversion_factors.keys())

# Conversion calculation
converted_value = value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# Display the result
st.write(f"### {value} {from_unit} = {converted_value:.5f} {to_unit}")
