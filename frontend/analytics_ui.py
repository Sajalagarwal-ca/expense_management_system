import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import mysql.connector



API_URL = "http://localhost:8000"


def analytics_category():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload)
        response = response.json()

        data = {
            "Category": list(response.keys()),
            "Total": [response[category]["total"] for category in response],
            "Percentage": [response[category]["percentage"] for category in response]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.title("Expense Breakdown By Category")

        st.bar_chart(data=df_sorted.set_index("Category")['Percentage'], width=0, height=0, use_container_width=True)

        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

        st.table(df_sorted)

def analytics_months():
    ############################################################
    # Approach 1
    ##############################################################
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="expense_manager"
    )
    cursor =connection.cursor()
    query = "select  month(expense_date) as num, date_format(expense_date, '%M') as MonthName ,sum(amount) as Total from expenses group by num, MonthName"
    cursor.execute(query)
    results =cursor.fetchall()
    
    df = pd.DataFrame(results, columns= ["Month Number", "Month Name", "Total Expenses"])
    df["Total Expenses"]=df["Total Expenses"].round()
    df_sorted = df.sort_values(by="Month Number")
    df_sorted =df_sorted.set_index("Month Number")
    st.title("Expense Breakdown By Months")
    st.bar_chart(data=df_sorted.set_index("Month Name")['Total Expenses'], width=0, height=0, use_container_width=True)
    st.table(df_sorted)

    cursor.close()
    connection.close()
    ###########################################################

    # Approach 2

    ##########################################################
    # response = requests.get(f"{API_URL}/monthly_summary/")
    # monthly_summary = response.json()

    # df = pd.DataFrame(monthly_summary)
    # df.rename(columns={
    #     "expense_month": "Month Number",
    #     "month_name": "Month Name",
    #     "total": "Total"
    # }, inplace=True)
    # df_sorted = df.sort_values(by="Month Number", ascending=False)
    # df_sorted.set_index("Month Number", inplace=True)

    # st.title("Expense Breakdown By Months")

    # st.bar_chart(data=df_sorted.set_index("Month Name")['Total'], width=0, height=0, use_container_width=True)

    # df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

    # st.table(df_sorted.sort_index())
    
   
