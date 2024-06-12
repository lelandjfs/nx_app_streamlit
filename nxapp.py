import os
import streamlit as st
import pandas as pd
import logging
import pymongo
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

username = os.getenv("MONGODB_USER")
password = os.getenv("MONGODB_PASSWORD")
cluster_url = os.getenv("MONGODB_CLUSTER_URL")

# MongoDB connection
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/?retryWrites=true&w=majority&appName=staging-lnkdn-raw")

db = client["linkedin"]
collection = db["connections-upload-streamlit"]

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

linkedin_url = st.text_input("Your Linkedin URL")

st.write("")
st.write("")

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose a file")
# submit button
upload_button = st.button('Submit')

# next steps: need a function that parses through the downloads + saves + appends their linkedin onto data
# need to find database
#need to set up and trial Bardeen

def main():
    # Check if the submit button is pressed
    if upload_button:
        # Check if the file is uploaded
        if uploaded_file is not None:
            try:
                # Process the uploaded file
                process_csv(uploaded_file, linkedin_url)
                st.success("File has been parsed successfully!")
            except Exception as e:
                # If an exception occurs during processing, display an error message
                st.error(f"An error occurred while processing the file: {str(e)}")
        else:
            # Display an error message if no file is uploaded
            st.error("Please upload a file before submitting.")

def process_csv(uploaded_file, linkedin_url):
    # Set up basic logging
    logging.basicConfig(level=logging.ERROR, filename='processing_errors.log', filemode='a',
                        format='%(asctime)s - %(levelname)s - %(message)s')

    expected_columns = ['First Name', 'Last Name', 'URL', 'Email Address', 'Company', 'Position', 'Connected On']
    new_column_names = ['FirstName', 'LastName', 'URL', 'EmailAddress', 'Company', 'Position', 'ConnectedOn']

    try:
        # Read the CSV file directly from the uploaded file
        data = pd.read_csv(uploaded_file, skiprows=3)

        # Check if the file contains the expected columns
        if list(data.columns) != expected_columns:
            raise ValueError("The file format is incorrect. Please provide a file with the expected column names.")

        # Rename the columns
        data.columns = new_column_names

        # Add new columns
        data['DateCollected'] = datetime.now().strftime("%Y-%m-%d")
        data['OwnerURL'] = linkedin_url

        # Save processed data to MongoDB
        store_data_mongodb(data)

    except Exception as e:
        logging.error(f"Error processing the CSV file: {e}")
        raise

def store_data_mongodb(data):
    try:
        # Convert dataframe to dictionary and insert into MongoDB
        collection.insert_many(data.to_dict('records'))
        logging.info("Data saved successfully to MongoDB")
    except Exception as e:
        logging.error(f"Error saving data to MongoDB: {e}")
        raise

if __name__ == "__main__":
    main()
