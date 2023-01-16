import streamlit as st
import pandas as pd
import datetime
import pickle
import statsmodels
from prophet import Prophet

models = {'Chinese' : pickle.load(open('chinese.pkl', 'rb')), 
        'French' : pickle.load(open('french.pkl', 'rb')), 
        'German' : pickle.load(open('german.pkl', 'rb')),
        'Spanish' : pickle.load(open('spanish.pkl', 'rb')),
        'Russian' : pickle.load(open('russian.pkl', 'rb')),
        'Japanese' : pickle.load(open('japanese.pkl', 'rb'))}

st.write(
    """
    # Web Traffic Forecast

    """
)

col1, col2, col3 = st.columns(3)

with col1:
    lang = st.selectbox('Select webpage language:', ('Chinese', 'French', 'German', 'Spanish', 'Russian', 'Japanese'))
with col2:
    strt_date = st.date_input(
    "Enter Start Date of Forecast",
    datetime.date(2017, 1, 1),
    min_value=datetime.date(2017, 1, 1))
with col3:
    end_date = st.date_input(
    "Enter End Date of Forecast",
    datetime.date(2017, 6, 30),
    min_value=datetime.date(2017, 1, 1)) 

tot_days = (end_date - datetime.date(2017, 1, 1)).days # Number of days to forecast
actual_days = (end_date - strt_date).days

dates = [strt_date + datetime.timedelta(days=i) for i in range(tot_days)]

st.write(f"""
#### {lang} forecast for {actual_days} days
""")

col4, col5 = st.columns(2)

with col4:
    if lang in ['Chinese', 'French', 'German', 'Spanish']:
        forecast = models[lang].forecast(tot_days)/10**6
        forecast_df = pd.DataFrame({'ds':dates, 'No.of.views(in 100k)':forecast}).reset_index(drop=True)
        st.dataframe(forecast_df[forecast_df.ds >= strt_date].reset_index(drop=True), width=500, height=350)
    else:
        future_dates = models[lang].make_future_dataframe(periods=tot_days,freq="D", include_history = False)
        forecast_df = models[lang].predict(future_dates)[['ds', 'yhat']]
        forecast_df.rename({'yhat':'No.of.views(in 100k)'}, axis=1, inplace=True)
        forecast_df['No.of.views(in 100k)'] = forecast_df['No.of.views(in 100k)']/10**6
        forecast_df['ds'] = dates
        st.dataframe(forecast_df[forecast_df.ds >= strt_date].reset_index(drop=True), width=500, height=350)

with col5:
    st.write(f"""
        #### Date vs No. of views
    """)

    st.line_chart(forecast_df.set_index('ds').loc[strt_date:, :])
