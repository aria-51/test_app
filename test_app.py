import streamlit as st

st.title('This is a Test')
st.title("This is not")


with st.form("myform"):
    topic_text = st.text_input("Enter prompt:", "")
    submitted = st.form_submit_button("Submit")