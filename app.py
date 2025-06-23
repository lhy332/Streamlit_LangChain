import os
import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the Google API key from the environment variables
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the Google Generative AI with the API key
genai.configure(api_key=api_key)

# Set the page configuration for the Streamlit app
st.set_page_config(
    page_title="Google Gemini Models by Harry",
    page_icon="🤖"
)

with st.sidebar:
    if 'GOOGLE_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        api_key = st.secrets['GOOGLE_API_KEY']
    else:
        api_key = st.text_input('Enter Google API Key:', type='password')
        if not (api_key.startswith('AI')):
            st.warning('Please enter your API Key!', icon='⚠️')
        else:
            st.success('Success!', icon='✅')
    os.environ['GOOGLE_API_KEY'] = api_key



st.title("🦜🔗 Harry's Gemini Quickstart App")

model = genai.GenerativeModel('gemini-pro')

with st.form("my_form"):
    input_text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not 'GOOGLE_API_KEY' in st.secrets:
        st.warning("Please enter your Google Gemini API key!", icon="⚠")
    if submitted and 'GOOGLE_API_KEY' in st.secrets:
        response = st.info(model.generate_content(input_text))
        print(f"Gemini's Response: {response}")