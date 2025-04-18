import streamlit as st
import openai
import requests

# Set your OpenRouter API Key here
openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

# Load the document (replace with your actual document)
# For example, loading a simple text file for now:
document_content = ""
with open('your_document.txt', 'r') as file:
    document_content = file.read()

# Set up Streamlit UI
st.title("📘 Document-Based AI Chatbot")
st.write("Ask anything about the document:")

# User input for asking questions
user_input = st.text_input("Your Question:")

if user_input:
    # Create a prompt for OpenRouter with the document and user input
    prompt = f"Based on the following document:\n{document_content}\n\nUser asks: {user_input}"

    # Send the prompt to OpenRouter API (or OpenAI API for GPT models)
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # You can switch to another model
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=150
    )
    
    # Display the chatbot’s answer
    answer = response.choices[0].message['content']
    st.write(answer)
