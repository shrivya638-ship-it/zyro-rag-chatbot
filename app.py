import streamlit as st

st.set_page_config(page_title="Zyro Dynamics HR Chatbot")

def hr_bot(query):
    query = query.lower()

    if "leave" in query:
        return """
        Leave Policy:
        Employees are entitled to Casual Leave, Sick Leave and other leave benefits
        as per Zyro Dynamics HR policies.
        """

    return "I can only answer questions based on Zyro Dynamics HR policy documents."

st.title("🤖 Zyro Dynamics HR Chatbot")

question = st.text_input("Ask an HR question")

if st.button("Ask"):

    answer = hr_bot(question)

    st.write(answer)
