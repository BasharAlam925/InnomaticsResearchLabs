import streamlit as st
import google.generativeai as genai

genai.configure(api_key='AIzaSyCHGvCV_UsrQLx8EZrb58IQ9qqQEyRNcYI')

sys_prompt = (
     "You are an AI Code Reviewer. "
    "Your task is to review code snippets provided by users. "
    "Provide detailed feedback, including suggestions for improvement, best practices, "
    "potential issues, and alternative approaches. "
    "If the code is well-written, acknowledge its quality and mention any additional improvements. "
    "Avoid reviewing non-code content and politely decline if the query is unrelated to code."
)

model = genai.GenerativeModel(
    model_name="models/gemini-2.0-flash-exp", 
    system_instruction=sys_prompt
)
st.title("Review your code with AI")
st.markdown(
    """
    Welcome to the **AI Code Reviewer**!
    Paste your code snippet below, and I'll provide a detailed review, including feedback and suggestions.  
    *Note: Please only submit code-related content.* 
    """
)
# user_prompt=st.text_input("Ask your query...")

user_code = st.text_area(label="Paste your code here:", placeholder="Enter your code snippet for review...")

btn_click=st.button("Review")

if btn_click==True:
    response = model.generate_content(user_code)
    st.success("✅ Code Review Generated!")
    st.write(response.text)

