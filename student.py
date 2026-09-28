import streamlit  as st
from datetime import date

st.title("STUDENT REGISTRATION FORM")

name=st.text_input("Enter Name")


age=st.number_input("Enter Age",min_value=0)

DOB=st.date_input("DOB",min_value=date(1990,1,1),
                max_value=date.today(),
                value=date(2000,1,1) )
email=st.text_input("Enter email")


gender=st.radio("Gender",["Male","Female"])
place=st.selectbox("Place",["Ernakulam","Thrissur","Alappuzha","Idukki"])
qualification=st.selectbox("Qualification",["java","dotnet","testing","developer"])

btn=st.button("REGISTER")
if btn:
    st.title("STUDENT REGISTRATION FORM")
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("DOB:",DOB)
    st.write("Email:",email)
    st.write("Gender:", gender)
    st.write("Place:", place)
    st.write("Qualification:",qualification)