import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the page configuration for the Streamlit app
st.set_page_config(
    page_title="Google Gemini Models by Harry",
    page_icon="🤖"
)

# Get the Google API key from the environment variables
api_key = st.sidebar.text_input("Gemini API Key", type="password")

# Configure the Google Generative AI with the API key
genai.configure(api_key=api_key)

st.title("🦜🔗 Harry's Gemini Quickstart App")

model = genai.GenerativeModel('gemini-2.5-flash')

with st.form("my_form"):
    input_text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not api_key:
        st.warning("Please enter your Google Gemini API key!", icon="⚠")
    if submitted and api_key:
        response = st.info(model.generate_content(input_text))
        print(f"Gemini's Response: {response}")