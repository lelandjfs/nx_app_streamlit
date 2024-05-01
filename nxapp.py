import streamlit as st
import pandas as pd
import logging

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
                process_csv(uploaded_file)
                st.success("File has been parsed successfully!")
            except Exception as e:
                # If an exception occurs during processing, display an error message
                st.error(f"An error occurred while processing the file: {str(e)}")
        else:
            # Display an error message if no file is uploaded
            st.error("Please upload a file before submitting.")

def process_csv(uploaded_file):
    # Set up basic logging will need to pip and import
    logging.basicConfig(level=logging.ERROR, filename='processing_errors.log', filemode='a',
                        format='%(asctime)s - %(levelname)s - %(message)s')

    expected_columns = ['First Name', 'Last Name', 'URL', 'Email Address', 'Company', 'Position', 'Connected On']
    new_column_names = ['first_name', 'last_name', 'url', 'email_address', 'company', 'position', 'connected_date']

    try:
        # Read the CSV file directly from the uploaded file
        data = pd.read_csv(uploaded_file, skiprows=3)

        # Check if the file contains the expected columns
        if list(data.columns) != expected_columns:
            raise ValueError("The file format is incorrect. Please provide a file with the expected column names.")

        # Rename the columns
        data.columns = new_column_names

        # Save processed data to a specified file location
        store_data_someplace(data)

    except Exception as e:
        logging.error(f"Error processing the CSV file: {e}")
        raise

def store_data_someplace(data):
    # Replace the placeholder string with the actual file path where you want to save the data
    file_path = (r'C:\Users\lelan\OneDrive\Documents\MySQL\Projects\Streamlit\Linkedin\Database\Database_Parsed_CSVs\logging.csv')
    data.to_csv(file_path, index=False)
    logging.info(f"Data saved successfully to {file_path}")

if __name__ == "__main__":
    main()
