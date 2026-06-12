
import streamlit as st

st.set_page_config(page_title="Zyro Dynamics HR Chatbot")

st.title("🤖 Zyro Dynamics HR Chatbot")

question = st.text_input("Ask an HR question")

if st.button("Ask"):

    answer = hr_bot(question)

    st.write(answer)
