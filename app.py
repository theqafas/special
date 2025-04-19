import streamlit as st
import google.generativeai as genai

# Set your Gemini API key here
genai.configure(api_key="AIzaSyCoHxGk58O0xDAPDhSCckYpNyYAiKquz5o")  # 🔑 Replace this with your key

# Load the document
with open("your_document.txt", "r", encoding="utf-8") as file:
    document_text = file.read()

# Initialize the Gemini model (1.5 Flash)
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("📄 Gemini 1.5 Flash - Document QA Bot")
st.write("Ask any question based on your uploaded document.")

# User input
user_question = st.text_input("Ask a question:")

if user_question:
    with st.spinner("Thinking..."):
        try:
            # Generate content using Gemini
            response = model.generate_content(f"""
You are an intelligent assistant. Use the following document to answer the question:

Document:
{document_text}

Question:
{user_question}
""")
            st.success(response.text)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
