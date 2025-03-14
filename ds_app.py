#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import google.generativeai as genai

# Configure Gemini AI
genai.configure(api_key="AIzaSyCHGvCV_UsrQLx8EZrb58IQ9qqQEyRNcYI")

# System prompt to keep AI focused on Data Science queries
sys_prompt = (
    "You are a helpful data science tutor. "
    "You must only resolve data science-related queries. "
    "If a user asks something unrelated, politely ask them to stay on topic."
)

# Initialize the AI model
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro",
    system_instruction=sys_prompt
)

# Streamlit UI
st.title("Your AI Data Science Tutor 🤖")
st.markdown(
    """
    Welcome! I'm here to help you with **Data Science-related** questions.  
    Just type your query below, and I'll do my best to provide an insightful answer.  
    **Note:** *Non-Data Science queries will be politely declined.*  
    """
)

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history dynamically
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(chat["question"])
    with st.chat_message("assistant"):
        st.write(chat["answer"])

# If an answer has been generated, move input box to the bottom
user_prompt = None  # Initialize user input variable

if "last_answer_generated" in st.session_state and st.session_state.last_answer_generated:
    st.session_state.last_answer_generated = False  # Reset flag
    user_prompt = st.text_area(label="**Ask Another Query:**", placeholder="Type here...")

else:
    user_prompt = st.text_area(label="**Ask your query:**", placeholder="Type here...")

# Button click action
if st.button("Generate Answer"):
    if user_prompt.strip():  # Ensure input is not empty
        # Prepare conversation history to maintain context
        conversation = "\n".join([f"User: {msg['question']}\nAI: {msg['answer']}" for msg in st.session_state.chat_history])
        full_prompt = f"{conversation}\nUser: {user_prompt}\nAI:"

        # Get response from AI model with memory
        response = model.generate_content(full_prompt)
        answer = response.text if response.text else "I'm unable to generate an answer right now."

        # Append to chat history
        st.session_state.chat_history.append({"question": user_prompt, "answer": answer})

        # Set flag to move input box to the bottom
        st.session_state.last_answer_generated = True
        st.rerun()  # Refresh the UI to move the input box down

    else:
        st.warning("Please enter a query before clicking the button.")

