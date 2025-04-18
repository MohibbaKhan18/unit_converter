import streamlit as st

st.title("Unit Converter")
st.write("Select a category, enter a value, and get the converted result in real-time.")
category = st.selectbox("Choose a category", ["Length", "Temperature", "Time"])
if category == "Length":
    unit = st.selectbox("Select conversion", [
        "Kilometers to Meters",
        "Meters to Kilometers",
        "Centimeters to Meters",
        "Meters to Centimeters"
    ])
elif category == "Temperature":
    unit = st.selectbox("Select conversion", [
        "Fahrenheit to Celsius",
        "Celsius to Fahrenheit"
    ])
elif category == "Time":
    unit = st.selectbox("Select conversion", [
        "Seconds to Minutes",
        "Minutes to Seconds",
        "Minutes to Hours",
        "Hours to Minutes",
        "Hours to Days",
        "Days to Hours"
    ])


value = st.number_input("Enter a value to convert", format="%.2f")

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Meters":
            return value * 1000
        elif unit == "Meters to Kilometers":
            return value / 1000
        elif unit == "Centimeters to Meters":
            return value / 100
        elif unit == "Meters to Centimeters":
            return value * 100

    elif category == "Temperature":
        if unit == "Fahrenheit to Celsius":
            return (value - 32) * 5.0 / 9.0
        elif unit == "Celsius to Fahrenheit":
            return (value * 9.0 / 5.0) + 32

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return "Invalid conversion"

# Convert button
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if isinstance(result, (int, float)):
        st.success(f"The result is: {result:.2f}")
    else:
        st.error("Something went wrong with the conversion.")
