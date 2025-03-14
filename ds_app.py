#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import google.generativeai as genai

genai.configure(api_key='AIzaSyCHGvCV_UsrQLx8EZrb58IQ9qqQEyRNcYI')

sys_prompt = (
    "You are a helpful data science tutor. "
    "You can only resolve data science-related queries. "
    "If someone asks queries unrelated to data science, "
    "politely ask them to ask relevant queries only."
)

model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro", 
    system_instruction=sys_prompt
)
st.title("Your AI Data Science Tutor 🤖")
st.markdown(
    """
    Welcome! I'm here to help you with **Data Science-related** questions.  
    Just type your query below, and I'll do my best to provide an insightful answer.  
    **Note:** *Non-Data Science queries will be politely declined.*  
    """
)
# user_prompt=st.text_input("Ask your query...")

user_prompt = st.text_area(label="**Ask your query:**", placeholder="Type here...")

btn_click=st.button("Generate Answer")

if btn_click==True:
    response=model.generate_content(user_prompt)
    st.success("✅ Answer Generated!")
    st.write("### AI Tutor's Answer:")
    st.write(response.text)

