import streamlit as st

st.title("AI Developer Network Map")


# Display the summary field
summary_placeholder = st.empty()

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose a file")