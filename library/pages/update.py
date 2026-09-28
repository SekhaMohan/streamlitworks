import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete
st.title("UPDATE A BOOK RECORD")
id=st.text_input("Enter Book ID")
title=st.text_input("title")
author=st.text_input("author")
price=st.number_input("price",min_value=0)
pages=st.number_input("pages",min_value=0)
language=st.text_input("language")
btn=st.button("UPDATE")
if btn:
    if id:
        b = BookListCreateRetrieveUpdateDelete()
        record = b.update(title,author,price,pages,language,id)

        if record==True:
            st.success("record is updated")
        else:
            st.warning("id not found")
    else:
        st.warning("please enter the book id")