import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("🦜🔗 Quickstart App")

openai_api_key = st.sidebar.text_input("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", type="password")


def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)