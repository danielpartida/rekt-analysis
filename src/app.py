from datetime import datetime
import streamlit as st
import pandas as pd

from main import run_main, get_count_statistics, get_plots

now = datetime.today()
now_str = now.strftime("%d/%m/%Y %H:%M")
st.set_page_config(page_title='Rekts Insights', page_icon="🧊", layout='centered', initial_sidebar_state='auto')
st.title('Visualization of Rekts')
st.text('Data fetched at {0} CET'.format(now_str))
st.header("Key statistics")

df_rekts, issue_type_count, category_count, year_count = run_main(limit=50, show_plots=False, save_plots=False)
main_issue, max_issue_pct = get_count_statistics(series_with_count=issue_type_count)
main_category, max_category_pct = get_count_statistics(series_with_count=category_count)
year_count.index = pd.DatetimeIndex(year_count.index).year
main_year, max_year_pct = get_count_statistics(series_with_count=year_count)

col1, col2, col3 = st.columns(3)
col1.write("{0} is the main issue of rekts with {1:.0%} of the time".format(main_issue, max_issue_pct))
col1.table(issue_type_count)
col2.write("{0} is the main category of rekts with {1:.0%} of the time".format(main_category, max_category_pct))
col2.table(category_count)
col3.write("{0} is the year where most rekts occurred with {1:.0%} of the time".format(main_year, max_year_pct))
col3.table(year_count)

fig_scatter_issue, fig_scatter_category = get_plots(df=df_rekts)
tab1_scatter, tab2_scatter = st.tabs(['Issue type', 'Category'])
with tab1_scatter:
    st.plotly_chart(fig_scatter_issue, use_container_width=True)

with tab2_scatter:
    st.plotly_chart(fig_scatter_category, use_container_width=True)
