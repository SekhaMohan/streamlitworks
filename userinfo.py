import streamlit  as st

st.title("WELCOME")

name=st.text_input("Enter Name")
st.write(name)

age=st.number_input("Enter Age",min_value=0)
st.write(age)

gender=st.radio("Gender",["Male","Female"])
place=st.selectbox("Place",["Ernakulam","Thrissur","Alappuzha"])
qualification=st.selectbox("Qualification",["BBA","MBA","BCA","MCA"])

btn=st.button("SUBMIT")
if btn:
    st.title("WELCOME")
    st.subheader("Name:",name)
    st.write("Age:",age)
    st.write("Gender:", gender)
    st.write("Place:", place)
    st.write("Qualification:",qualification)


