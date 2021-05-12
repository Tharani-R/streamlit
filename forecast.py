import pandas as pd
import numpy as np
import datetime
import streamlit as st
from pmdarima import auto_arima
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt 


def forecast_vader(tweets):
    tweet_user = pd.DataFrame()
    tweet_user = tweets.groupby(['username','date'],as_index=False).agg({'vader_score':'mean'})

    return tweet_user


def forecast_date(tweets):
    tweets['date']= pd.to_datetime(tweets['date'])
    frames = []
    for loc in tweets.username.unique():
        frames.append(pd.DataFrame(data={'username' : loc, 
                                        'date' : pd.date_range(start=tweets.date.min(), end=tweets.date.max())}))
        df_combined = pd.concat(frames)
        tweets = pd.merge(df_combined, tweets, how='left', left_on=['username','date'], right_on=['username','date'])
    
    tweets.fillna(0, inplace=True)

    return tweets

def forecast_model(tweets):
    stepwise_fit = auto_arima(tweets.vader_score, start_p = 1, 
                          start_q = 1,	max_p = 3, max_q = 3, 
                          m = 12, start_P = 0, seasonal = True,
                          d = None, D = 1, trace = True, 
                          error_action ='ignore', 
                          # we don't want to know if an order does not work 
                          suppress_warnings = True, 
                          # we don't want convergence warnings
                          information_criterion='aic',
                          stepwise = True)
    model=SARIMAX(tweets.vader_score,order=stepwise_fit.order,seasonal_order=stepwise_fit.seasonal_order)
    model_fit=model.fit()
    forecasting = model_fit.forecast(7)

    return forecasting

def forecast_plot(tweets, forecast):
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.plot((tweets['vader_score']))
    ax.plot((forecast))
    st.pyplot(fig)

def forecast_user(tweets):
    tweet_user = forecast_vader(tweets)
    tweets = forecast_date(tweet_user)

    return tweets