import streamlit as st
import openai

# Set OpenRouter API key and base
openai.api_key = "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" 
openai.api_base = "https://openrouter.ai/api/v1"

# Load the document
with open("your_document.txt", "r", encoding="utf-8") as file:
    document_text = file.read()

st.title("📄 Document QA Bot")
st.write("Ask questions based on the uploaded document.")

# User input
user_question = st.text_input("Ask a question:")

if user_question:
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="openai/gpt-3.5-turbo",  # You can replace with another OpenRouter-supported model
                messages=[
                    {"role": "system", "content": f"You are an assistant who answers questions based on the following document:\n\n{document_text}"},
                    {"role": "user", "content": user_question},
                ]
            )
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {str(e)}")
