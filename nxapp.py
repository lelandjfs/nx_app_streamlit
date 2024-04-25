import streamlit as st

st.title("AI Developer Network Map")


summary_text = "Generate a network graph of your connections to some of the most exciting AI companies."

sub_text1 = "Input your personal Linkedin URL and navigate to [THIS LINK] (https://www.linkedin.com/mypreferences/d/download-my-data) (or following the directions below) to request a download of your Linkedin contacts and profile data. It may take a few minutes for the download to be sent to the email you use for your Linkedin."

sub_text2 = "*Settings & Privacy --> Data Privacy --> Get a copy of your data*; **Select both Connections and Profile buttons**."

# Display the summary field
summary_placeholder = st.header(summary_text)

st.write("")
st.write("")
st.write("")

st.markdown(sub_text1)
st.write("")
st.markdown(sub_text2)

st.write("")
st.write("")
st.write("")

st.text_input("Your Linkedin URL")

st.write("")
st.write("")

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose a file")


# next steps: need a function that parses through the downloads + saves + appends their linkedin onto data
# need to find database
#need to set up and trial Bardeen