import streamlit as st

# Conversion factors for different unit types
unit_categories = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701
    },
    "Mass": {
        "Gram": 1,
        "Kilogram": 0.001,
        "Milligram": 1000,
        "Pound": 0.00220462,
        "Ounce": 0.035274
    },
    "Temperature": {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x * 9/5) + 32,
        "Kelvin": lambda x: x + 273.15
    }
}

st.title("Unit Converter")

# User selects unit category
category = st.selectbox("Select Category:", unit_categories.keys())

# Get the corresponding conversion factors or formulas
conversion_factors = unit_categories[category]

# User input for value
value = st.number_input("Enter value:", min_value=0.0, value=1.0, step=0.1)

# Dropdowns for selecting units
from_unit = st.selectbox("From Unit:", conversion_factors.keys())
to_unit = st.selectbox("To Unit:", conversion_factors.keys())

# Conversion calculation
if category == "Temperature":
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        converted_value = (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        converted_value = value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        converted_value = (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        converted_value = (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        converted_value = value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        converted_value = (value - 273.15) * 9/5 + 32
    else:
        converted_value = value
else:
    converted_value = value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# Display the result
st.write(f"### {value} {from_unit} = {converted_value:.5f} {to_unit}")
