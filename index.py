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
    },
    "Area": {
        "Square Meter": 1,
        "Square Kilometer": 0.000001,
        "Square Mile": 3.861e-7,
        "Square Yard": 1.19599,
        "Square Foot": 10.7639
    },
    "Data Transfer Rate": {
        "Bits per second": 1,
        "Kilobits per second": 0.001,
        "Megabits per second": 0.000001,
        "Gigabits per second": 1e-9
    },
    "Digital Storage": {
        "Byte": 1,
        "Kilobyte": 0.001,
        "Megabyte": 1e-6,
        "Gigabyte": 1e-9,
        "Terabyte": 1e-12
    },
    "Energy": {
        "Joule": 1,
        "Kilojoule": 0.001,
        "Calorie": 0.239006,
        "Kilocalorie": 0.000239006
    },
    "Frequency": {
        "Hertz": 1,
        "Kilohertz": 0.001,
        "Megahertz": 1e-6,
        "Gigahertz": 1e-9
    },
    "Fuel Economy": {
        "Kilometers per Liter": 1,
        "Miles per Gallon": 2.35215
    },
    "Plane Angle": {
        "Degree": 1,
        "Radian": 0.0174533
    },
    "Pressure": {
        "Pascal": 1,
        "Bar": 1e-5,
        "PSI": 0.000145038
    },
    "Speed": {
        "Meter per second": 1,
        "Kilometer per hour": 3.6,
        "Mile per hour": 2.23694
    },
    "Time": {
        "Second": 1,
        "Minute": 1/60,
        "Hour": 1/3600,
        "Day": 1/86400
    },
    "Volume": {
        "Liter": 1,
        "Milliliter": 1000,
        "Cubic Meter": 0.001,
        "Cubic Foot": 0.0353147
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
