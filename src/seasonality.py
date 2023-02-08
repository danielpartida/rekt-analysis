import pandas as pd
from prophet import Prophet

from main import run_main

df_rekts, issue_count, issue_type_mean, category_count, category_mean, upper_category_count, upper_category_mean, year_count = run_main(limit=100, show_plots=True)

m = Prophet()
year_count = pd.DataFrame(year_count, columns=['y'])
year_count.reset_index(inplace=True)
year_count.rename(columns={'date': 'ds'}, inplace=True)
m.fit(year_count)

# Make rekt forecast for the next 3 months
future = m.make_future_dataframe(periods=100)

forecast = m.predict(future)
fig, ax = m.plot_components(forecast)