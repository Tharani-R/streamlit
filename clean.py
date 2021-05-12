import pandas as pd
import numpy as np
import re
import datetime

#function to remove hyperlinks
def clean_link(text):
    text = re.sub('https://([a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '',  text)
    text = text.lower()
    return text

#function to remove symbols
def clean_symbol(text):
    text = re.sub('[$-_@.&+!*\(\),#`''"~]', '', text)
    text = text.rstrip()
    return text

#function to remove reply usernames
def clean_username(tweets):
    tweet = []
    for i in tweets.tweet:
        words = i.split(' ')
        filtered_sentence = []
        for j in words:
            if j.startswith('@') == False:
                filtered_sentence.append(j)
        filtered_sentence = ' '.join(filtered_sentence)
        tweet.append(filtered_sentence)
    tweets['tweet'] = tweet
    
    return tweets

def clean_date(tweets):

    for i in range(0,len(tweets)):
        try:
            if datetime.datetime.strptime(tweets["date"][i],'%Y-%m-%d'):
                tweets["date"][i] = datetime.datetime.strptime(tweets["date"][i],'%Y-%m-%d').strftime('%Y-%m-%d')
        except:
            tweets["date"][i] = datetime.datetime.strptime(tweets["date"][i],'%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        
    
    return tweets

def clean(tweet):
    tweet = clean_username(tweet)
    tweet['tweet'] = tweet['tweet'].apply(clean_link)
    tweet['tweet'] = tweet['tweet'].apply(clean_symbol)
    tweet['tweet'].replace(r'^\s*$', np.nan, regex=True, inplace=True)
    tweet = tweet.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))
    tweet = clean_date(tweet)

    return tweet