import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("SEARCH A BOOK RECORD")
id=st.text_input("Enter Book ID")
btn=st.button("Show Details")
if btn:
    if id:
        b=BookListCreateRetrieveUpdateDelete()
        record=b.retrieve(id)
        if record:
            st.write("Title",record[1])
            st.write("Author", record[2])
            st.write("Price", record[3])
            st.write("pages",record[4])
            st.write("language", record[5])
        else:
            st.warning("record not found")
    else:
        st.warning("please enter the book id")