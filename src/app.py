import streamlit as st

st.set_page_config(page_title='Rekts Insights', page_icon="🧊", layout='centered', initial_sidebar_state='auto')

st.title('Rekts Analysis')

# FIXME: Avoid opening a new tab or remove hyperlinks
st.markdown('''
This app is structured in two pages
### The [key insights](/Key_Insights) shows
- shows live key metrics
- Statistics
- Most vulnerable rekt issue types, categories, and more
- Which issue types / categories exhibit the most rekts
- Which issue types / categories have the largest lost funds
- Which issue types / categories have the most recovered funds
### The [text insights](Text_Insights) shows NLP analysis like
- Topic modelling
''')
