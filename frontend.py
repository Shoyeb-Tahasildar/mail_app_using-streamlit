import streamlit as st

with st.form("my_form"):
   st.write("Inside the form")
   st.title('Simple email send web app: ')
   st.title('Please enter a :blue[email] to send :')
   send_emai_to = st.text_input("Reciver Email: ")
   message = st.text_input("Enter Content to send: ")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       pass
st.write("Outside the form")