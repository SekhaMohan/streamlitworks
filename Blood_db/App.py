import streamlit as st
from blood_db import Blood_donor
from datetime import date

tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','VIEW','RETRIEVE','DELETE','UPDATE'])
b=Blood_donor()
with tab1:
    st.title("ADD")
    name = st.text_input("name")
    blood_group = st.text_input("blood group")
    phone = st.number_input("phone", min_value=0)
    city = st.text_input("city")
    last_don = st.date_input("last date donation",min_value= date(1990,1,1),
                                                    max_value=date.today(),
                                                    value=date(2026,1,1),key="add_date")
    btn = st.button("ADD")
    if btn:
        b = Blood_donor()
        b.post(name,blood_group,phone, city, last_don)
        st.success("Record created successfully")
with tab2:
    st.title("VIEW")
    b = Blood_donor()
    records = b.get()
    st.table(records)
with tab3:
    st.title("RETRIEVE")
    id = st.text_input("Enter Donor ID",key="search_id")
    btn = st.button("Show Details")
    if btn:
        if id:
            b = Blood_donor()
            record = b.retrieve(id)
            if record:
                st.write("Name", record[1])
                st.write("Blood Group", record[2])
                st.write("Phone", record[3])
                st.write("Place", record[4])
                st.write("Last Date Donation", record[5])
            else:
                st.warning("record not found")
        else:
            st.warning("please enter the donor id")
with tab4:
    st.title("DELETE")
    id = st.text_input("Enter Donor ID")
    btn = st.button("DELETE")
    if btn:
        if id:
            b = Blood_donor()
            record = b.delete(id)
            if record == True:
                st.success("record is deleted")
            else:
                st.warning("No record found")
        else:
            st.warning("donor id not found")
with tab5:
    st.title("UPDATE")
    id = st.number_input("Enter Donor ID",min_value=0)
    name = st.text_input("Name")
    blood_group = st.text_input("Blood Group")
    phone = st.number_input("Phone", min_value=0)
    city = st.text_input("City")
    last_don = st.date_input("last date donation",min_value= date(1990,1,1),
                                                    max_value=date.today(),
                                                    value=date(2026,1,1),key="update date")
    btn = st.button("UPDATE")
    if btn:
        if id:
            b = Blood_donor()
            record = b.put(name,blood_group, phone,city, last_don, id)
            if record==True:
                st.success("record is updated")
            else:
                st.warning("id not found")
        else:
            st.warning("please enter the donor id")