import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

st.title("Expense Management System")
# st.header("Header")
# st.subheader("Sub Header")
# st.text("Text")
# st.table(data = [['tom', 10], ['nick', 15], ['juli', 14]]
# )
# st.line_chart(data=[1,5,8,9,10])

tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
        st.write(existing_expenses)
    else:
        st.error("Failed to retrieve expenses")
        existing_expenses = []
    
    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Category")
        with col2:
            st.text("Amount")
        with col3:
            st.text("Notes")



