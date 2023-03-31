

# this is import data
import smtplib
import ssl
import streamlit as st
import mysql.connector as con
smtp_port  = 587
smtp_server = "smtp.gmail.com"
email_from = "" #sender mail
pwd  = "" #get the password authentication string form google dash board
simple_email_context = ssl.create_default_context()



# databse connectivity
try:
    db = con.connect(
        host="localhost", #ip of 
        user="root", #user name
        password = "", #db password
        database = "" #databse name
    )
    print(db.get_server_info())
    curser = db.cursor()
except:
    print("database connection lost")

#function to save the data to the database
def saveData(send_emai_to,message):
    email_from = "" # sender email
    # send_emai_to = send_emai_to
    # message = message
    print(message)
    queory = ("INSERT INTO mail_data (senderMail,reciverMail,context) VALUES (%s,%s,%s)")
    data = (email_from,send_emai_to,message)

    try:
        curser.execute(queory, data)
        db.commit()
        curser.close()
        db.close()
    except:
        print("query not executed")
#mail send function
def sendmail(send_emai_to,message):
    try:
        print("connecting to server ...")
        tie_server = smtplib.SMTP(smtp_server,smtp_port)
        tie_server.starttls(context = simple_email_context)
        tie_server.login(email_from,pwd)
        print(send_emai_to+" "+message)
        print("connecting to server succesfull")
        tie_server.sendmail(email_from,send_emai_to,message)
        saveData(send_emai_to,message)
        return True
    except:
        print("Connection time out......")
    return False

#streamlit form
with st.form("my_form"):
   st.write("Inside the form")
   st.title('Simple email send web app: ')
   st.title('Please enter a :blue[email] to send :')
   send_emai_to = st.text_input("Reciver Email: ")
   message = st.text_input("Enter Content to send: ")
   submitted = st.form_submit_button("Submit")
   if submitted:
       try:
           if sendmail(send_emai_to, message):
               st.success("mail send succesfully")
           else :
               st.error("mail intrupted")
           saveData(send_emai_to, message)
       except:
           print("some error")










