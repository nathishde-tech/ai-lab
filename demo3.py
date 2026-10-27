import streamlit as st

from google import genai

st.title("My Gemini Chatbot")

st.write("Ask a question and Gemini will answer.")

API_KEY = st.secrets["GEMENINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

query = st.text_input("Enter your question")

if st.button("Ask Gemini"):

  if query.strip():

     with st.spinner("Gemini is thinking..."):

      response = client.models.generate_content(

       model="gemini-3.8-flash",

       contents=query
      )

     st.subheader("Gemini's Answer")

     st.write(response.text)

else:

 st.warning("Please enter a question.")