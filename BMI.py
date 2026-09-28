import streamlit  as st

st.title("BMI")
weight=st.number_input("enter weight",min_value=0)
print(weight)
height=st.number_input("enter height",min_value=0)
print(height)
btn=st.button("BMI CALCULATOR")

if btn:
    result = weight/((height/100)**2)
    st.write("BMI", result)
    if result<18.5:
        st.info("Under Weight")
    elif 18.5<=result<30:
        st.success("Normal")
    elif 25<=result<30:
        st.warning("Overweight")
    else:
        st.error("Obesity")