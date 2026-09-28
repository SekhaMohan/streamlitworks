import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("DELETE A BOOK RECORD")
id=st.text_input("Enter Book ID")
btn=st.button("DELETE")
if btn:
    if id:
        b=BookListCreateRetrieveUpdateDelete()
        record=b.delete(id)
        if record==True:
            st.success("record is deleted")
        else:
            st.warning("No record found")
    else:
        st.warning("book id not found")
