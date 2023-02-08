from datetime import datetime
import streamlit as st
import pandas as pd

from main import get_count_statistics, run_main, get_plots

now = datetime.today()
now_str = now.strftime("%d/%m/%Y %H:%M")
st.set_page_config(page_title='Rekts Insights', page_icon="🧊", layout='centered', initial_sidebar_state='auto')
st.title('Rekts Analysis')
st.text('Data fetched at {0} CET'.format(now_str))

# Fetch data from the main script
# FIXME: Change limit back to 1000
df_rekts, issue_type_count, issue_type_mean, sub_category_count, sub_category_mean, upper_category_count, upper_category_mean, year_count = run_main(limit=100, show_plots=False)

# Prepare visualization plots
lost_returned_mean = df_rekts.mean()
main_issue, max_issue_pct = get_count_statistics(series_with_count=issue_type_count)
main_sub_category, max_sub_category_pct = get_count_statistics(series_with_count=sub_category_count)
main_upper_category, max_upper_category_pct = get_count_statistics(series_with_count=upper_category_count)
year_count.index = pd.DatetimeIndex(year_count.index).year
main_year, max_year_pct = get_count_statistics(series_with_count=year_count)
df_upper_category_count = pd.DataFrame(upper_category_count, columns=['count'])
df_sub_category_count = pd.DataFrame(sub_category_count, columns=['count'])
df_issue_count = pd.DataFrame(issue_type_count, columns=['count'])
df_year_count = pd.DataFrame(year_count, columns=['count'])

# Build Streamlit components
col1, col2 = st.columns(2)
col1.metric("Average  lost funds per rekt in $", "{0:,}".format(lost_returned_mean[0]))
col2.metric("Average returned funds after a rekt occurred in $", "{0:,}".format(lost_returned_mean[1]))

st.subheader("Rekts have an increasing trend peaking at {0} occurrences in {1}".format(year_count.max(), main_year))
st.line_chart(df_year_count)

st.text('So far {0:,} dollars have been lost by rekts, and {1:,} dollars have been returned'.format(
    df_rekts.fundsLost.sum(), df_rekts.fundsReturned.sum())
)
# Future work: Plot cummulative losses
# st.line_chart(df_cum_sum)

fig_scatter_issue, fig_scatter_sub_category, fig_scatter_upper_category = get_plots(df=df_rekts)

st.header('Data per category, issue type, and more')
# Future work: Create analysis for chains and token tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(['Issue type', 'Upper category', 'Sub-category', 'Token', 'Chain'])
with tab1:
    st.subheader("{0} is the most common rekt issue type with {1:.0%} of the time".format(main_issue, max_issue_pct))
    st.bar_chart(df_issue_count)
    st.subheader("The most vulnerable issue type is {0} where the average funds lost per rekt are {1:,} dollars".format(
        issue_type_mean.fundsLost.idxmax(), round(issue_type_mean.fundsLost.max(), 2)
    ))
    st.write("{0} is the issue type with the least amount of funds returned with {1:.0%} of the funds returned".format(
        (issue_type_mean['fundsReturned']/issue_type_mean['fundsLost']).idxmin(),
        round(min(issue_type_mean['fundsReturned'] / issue_type_mean['fundsLost']), 2)
    ))
    st.write("{0} is the issue type with the most amount of funds returned with {1:.0%} of the funds returned".format(
        (issue_type_mean['fundsReturned'] / issue_type_mean['fundsLost']).idxmax(),
        round(max(issue_type_mean['fundsReturned'] / issue_type_mean['fundsLost']), 2)
    ))
    st.bar_chart(issue_type_mean)
    st.plotly_chart(fig_scatter_issue, use_container_width=True)

with tab2:
    st.subheader("{0} is the most upper-rekt category with {1:.0%} of the time".format(main_upper_category, max_upper_category_pct))
    st.bar_chart(df_upper_category_count)
    st.subheader("The most vulnerable upper-category is {0} where the average lost funds per rekt are {1:,} dollars".format(
        upper_category_mean.fundsLost.idxmax(), round(upper_category_mean.fundsLost.max(), 2)
    ))
    st.write("{0} is the upper-category with the most amount of funds returned with {1:.0%} of the funds returned".format(
        (upper_category_mean['fundsReturned'] / upper_category_mean['fundsLost']).idxmin(),
        round(min(upper_category_mean['fundsReturned'] / upper_category_mean['fundsLost']), 2)
    ))
    st.write("{0} is the upper-category with the least amount of funds returned with {1:.0%} of the funds returned".format(
        (upper_category_mean['fundsReturned'] / upper_category_mean['fundsLost']).idxmax(),
        round(max(upper_category_mean['fundsReturned'] / upper_category_mean['fundsLost']), 2)
    ))
    st.bar_chart(upper_category_mean)
    st.plotly_chart(fig_scatter_upper_category, use_container_width=True)


with tab3:
    st.subheader("{0} is the most rekt sub-category with {1:.0%} of the time".format(main_sub_category, max_sub_category_pct))
    st.bar_chart(df_sub_category_count)
    st.subheader("The most vulnerable sub-category is {0} where the average lost funds per rekt are {1:,} dollars".format(
        sub_category_mean.fundsLost.idxmax(), round(sub_category_mean.fundsLost.max(), 2)
    ))
    st.write("{0} is the sub-category with the most amount of funds returned with {1:.0%} of the funds returned".format(
        (sub_category_mean['fundsReturned'] / sub_category_mean['fundsLost']).idxmin(),
        round(min(sub_category_mean['fundsReturned'] / sub_category_mean['fundsLost']), 2)
    ))
    st.write("{0} is the sub-category with the least amount of funds returned with {1:.0%} of the funds returned".format(
        (sub_category_mean['fundsReturned'] / sub_category_mean['fundsLost']).idxmax(),
        round(max(sub_category_mean['fundsReturned'] / sub_category_mean['fundsLost']), 2)
    ))
    st.bar_chart(sub_category_mean)
    st.plotly_chart(fig_scatter_sub_category, use_container_width=True)

with tab4:
    st.text("Future work...")

with tab5:
    st.text("Future work...")
