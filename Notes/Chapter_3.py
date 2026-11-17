import streamlit as st
st.markdown("# Welecome to Tea App")
st.markdown("You can learn_______________________")

# App title for the tea poll
st.title("Tea Taste Poll")

# Create two columns for tea names at the top
ctit1, ctit2 = st.columns(2)
with ctit1:
    st.header("Masala Tea")
with ctit2:
    st.header("Adarak Tea")

# Create two columns to display tea images and voting buttons
col1, col2 = st.columns(2, vertical_alignment="bottom")
with col1:
    st.image("https://images.pexels.com/photos/20270270/pexels-photo-20270270.jpeg", use_container_width=True)
    vote1 = st.button("Vote Masala Tea", use_container_width=True)
with col2:
    st.image("https://images.pexels.com/photos/34928359/pexels-photo-34928359.jpeg", use_container_width=True)
    vote2 = st.button("Vote Adarak Tea", use_container_width=True)

# Show a success message based on the selected vote
if vote1:
    st.success("Thnaks for voting Masla Tea")
elif vote2:
    st.success("Thanks for voting Adarak Tea")

# Sidebar inputs for user name and tea selection
name = st.sidebar.text_input("Enter Your Name", placeholder="Raza")
tea = st.sidebar.selectbox(
    "Make Your Tea",
    ["Masala Tea ", "Adarak Tea", "Lemon Tea", "Milk Tea", "Pakistani Tea"],
    index=None,
    placeholder="Select Tea:",
)

# Show a personalized confirmation when a tea is selected
if tea != None:
    st.sidebar.success(f"Hi {name}, Thanks for selecting {tea}, It will be ready soon")

# Expandable instructions section for making tea
with st.expander("Show Tea Making Instructions"):
    st.write("""
    1. Boil water with tea leaves
    2. Add milk and spices
    3. Serve hot
    """)