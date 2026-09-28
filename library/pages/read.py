import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("READ A BOOK RECORD")
# from library_db import BookListCreatRetrieveUpdateDelete
b=BookListCreateRetrieveUpdateDelete()
records=b.list()
st.table(records)

