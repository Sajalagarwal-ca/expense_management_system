import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_category
from analytics_ui import analytics_months


st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics by Category", "Analytics by Months"])

with tab1:
    add_update_tab()

with tab2:
    analytics_category()

with tab3:
    analytics_months()


