from datetime import datetime
import streamlit as st
import pandas as pd

from main import run_main, get_count_statistics

now = datetime.today()
now_str = now.strftime("%d/%m/%Y %H:%M")
st.set_page_config(page_title='Rekts Insights', page_icon="🧊", layout='centered', initial_sidebar_state='auto')
st.title('Visualization of Rekts')
st.text('Data fetched at {0}'.format(now_str))
st.header("Key statistics")

df, issue_type_count, category_count = run_main(limit=50, show_plots=False, save_plots=False)
main_issue, max_issue_percentage = get_count_statistics(series_with_count=issue_type_count)
main_category, max_category_percentage = get_count_statistics(series_with_count=category_count)

col1, col2, col3 = st.columns(3)
col1.write("{0} is the main issue of rekt occurring {1:.0%} of the time".format(main_issue, max_issue_percentage))
col1.table(issue_type_count)
col2.write("{0} is the main category of rekt occurring {1:.0%} of the time".format(main_category, max_category_percentage))
col2.table(category_count)
