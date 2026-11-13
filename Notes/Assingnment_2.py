import streamlit as st
import datetime as dt

# Get today's date so we can limit the date input to a valid range.
current_date = dt.date.today()

# Display the app title.
st.title("Age Calculator")

# Allow the user to choose a birth date.
# The minimum date is set to 1973, and the maximum is today's date.
dob = st.date_input(
    "Enter Your Date of Birth",
    min_value=dt.date(1973, 1, 1),
    max_value=current_date,
)

# Show a helpful note for users who cannot scroll far enough in the date picker.
st.write(":green[If dropdown not going back than 20 years , **Type manually or select oldest to get more**]")

# Show the selected date when a valid date is chosen.
if dob is not None:
    st.write(f"Selected : {dob}")

# Calculate the age by subtracting the birth year and adjusting for birthdays not yet reached.
age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))

# Display the computed age.
st.write(f"Your age is {age}")