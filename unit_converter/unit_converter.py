import streamlit as st

st.title("Unit Converter")
st.markdown("### Converts unit of Length, Temperature and Time.")
st.write("Select the type of conversion from the dropdown menu below.")

category = st.selectbox("Select a category", ["Length", "Temperature", "Time"])

def convertUnits(category,value,unit):
    if category == "Length":
        if unit == "meter to feet":
            return value * 3.28
        elif unit == "meter to inches":
            return value * 39.36
        elif unit == "meter to centimeter": 
            return value * 100
        elif unit == "meter to milimeter":
            return value * 1000
        elif unit == "feet to meter":
            return value / 3.28
        elif unit == "inches to meter":
            return value / 39.36
        elif unit == "centimeter to meter":
            return value / 100
        elif unit == "milimeter to meter":
            return value / 1000
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Celsius to Kelvin":
            return value + 273
        elif unit == "Kelvin to Celsius":
            return value - 273
        if unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60
        if unit == "seconds to hours":
            return value / 3600
        if unit == "hours to seconds":
            return value * 3600
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hours to minutes":
            return value * 60
        elif unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24
        
if category == "Length":
    unit = st.selectbox("📏Select unit", ["meter to feet", "feet to meter", "meter to inches", "inches to meter", "meter to centimeter", "centimeter to meter", "meter to milimeter", "milimeter to meter"])
elif category == "Temperature":
    unit = st.selectbox("🌡Select unit", ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius"])
elif category == "Time":
    unit = st.selectbox("⏱Select unit", ["seconds to minutes", "minutes to seconds", "seconds to hours", "hours to seconds", "minutes to hours", "hours to minutes", "hours to days", "days to hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result= convertUnits(category,value,unit)
    st.success(f"{str(value) + ' ' + unit.split('to')[0]} = {str(result) + ' ' + unit.split('to')[1]}")
