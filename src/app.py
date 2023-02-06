import streamlit as st
import pandas as pd

from main import run_main

st.title('Visualization of Rekts')
st.header("Key statistics")

df, issue_type_count, category_count = run_main(show_plots=False, save_plots=False)

st.write("Since 2013, there were {0} rekts".format(issue_type_count))
