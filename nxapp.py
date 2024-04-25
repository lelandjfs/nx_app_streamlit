import streamlit as st

st.title("AI Developer Network Map")


summary_text = "The purpose of this app is to generate a network graph of an inputted Linkedin connections download CSV."

# Display the summary field
summary_placeholder = st.header(text)

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose a file")
