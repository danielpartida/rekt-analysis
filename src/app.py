from datetime import datetime
import streamlit as st
import pandas as pd

from main import run_main, get_count_statistics, get_plots

now = datetime.today()
now_str = now.strftime("%d/%m/%Y %H:%M")
st.set_page_config(page_title='Rekts Insights', page_icon="🧊", layout='centered', initial_sidebar_state='auto')
st.title('Rekts Analysis')
st.text('Data fetched at {0} CET'.format(now_str))
st.header("Key statistics")

df_rekts, issue_type_count, issue_type_mean, category_count, category_mean, year_count = run_main(
    limit=50, show_plots=False, save_plots=False)
lost_returned_mean = df_rekts.mean()
main_issue, max_issue_pct = get_count_statistics(series_with_count=issue_type_count)
main_category, max_category_pct = get_count_statistics(series_with_count=category_count)
year_count.index = pd.DatetimeIndex(year_count.index).year
main_year, max_year_pct = get_count_statistics(series_with_count=year_count)
df_category_count = pd.DataFrame(category_count, columns=['count'])
df_issue_count = pd.DataFrame(issue_type_count, columns=['count'])
df_year_count = pd.DataFrame(year_count, columns=['count'])

st.write("{0:,} dollars is the average lost funds per rekt".format(lost_returned_mean[0]))
st.write("{0:,} is the average returned funds after a rekt occurred".format(lost_returned_mean[1]))

st.subheader("Rekts have an increasing trend peaking in {0}".format(main_year))
st.line_chart(df_year_count)

fig_scatter_issue, fig_scatter_category = get_plots(df=df_rekts)

st.header('Check in detail category, issue type and more')
# TODO: Create tbas by chain and/or token
tab1_scatter, tab2_scatter = st.tabs(['Issue type', 'Category'])
with tab1_scatter:
    st.subheader("{0} is the main issue of rekts with {1:.0%} of the time".format(main_issue, max_issue_pct))
    st.bar_chart(df_issue_count)
    st.subheader("The most vulnerable issue type is {0} where the average funds lost per rekt are {1:,} dollars".format(
        issue_type_mean.fundsLost.idxmax(), round(issue_type_mean.fundsLost.max(), 2)
    ))
    st.bar_chart(issue_type_mean)
    st.plotly_chart(fig_scatter_issue, use_container_width=True)

with tab2_scatter:
    st.subheader("{0} is the main category of rekts with {1:.0%} of the time".format(main_category, max_category_pct))
    st.bar_chart(df_category_count)
    st.subheader("The most vulnerable category is {0} where the average lost funds per rekt are {1:,} dollars".format(
        category_mean.fundsLost.idxmax(), round(category_mean.fundsLost.max(), 2)
    ))
    st.bar_chart(category_mean)
    st.plotly_chart(fig_scatter_category, use_container_width=True)
