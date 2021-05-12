import streamlit as st
import pandas as pd
from scrap import *
from clean import *
from nlp import *
from tweetLevel import *
from userLevel import *
from feature import *
from forecast import *

def main():
    st.title("DEPTECTOR")
    html_temp = """
    <div style="background-color:green;padding:2px">
    <h2 style="color:white;text-align:center;">App to detect Depression</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    username = st.text_input("USERNAME","")
    result=pd.DataFrame()
    userlevel = pd.DataFrame()
    user_groupby = pd.DataFrame()
    forecast = pd.DataFrame()
    depression = ''
    if st.button("Predict"):
        #try:
            if len(username) == 0:
                st.error("Enter valid Username")
            else:
                result = scrap_tweet(username)
                result = clean(result)
                result = feature(result)
                result = nlp_clean(result)
                result = tweetLevel(result)
                userlevel = feature_user(result)
                depression = userLevel(userlevel)
                st.success('The User is {}'.format(depression))
                if depression == "Depressed":
                    user_groupby = forecast_user(result)
                    forecast =forecast_model(user_groupby)
                    forecast_plot(user_groupby, forecast)
        #except ValueError:
            #st.error("Please enter a valid input")
        #print(result)
    #st.success('The output is '.format(result))
    
    #st.success('The forecast is {}'.format(forecast))
    #st.table(result)
    #st.table(userlevel)
    #st.table(forecast)
    
    
        

if __name__=='__main__':
    main()
