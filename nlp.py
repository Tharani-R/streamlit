import pandas as pd
import numpy as np
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import pycountry
from sklearn.feature_extraction.text import CountVectorizer
import os

nltk.download('punkt')

noneed = ['i', 'me', 'my', 'myself', 'mine', 'we', 'our', 'ours', 'im',
                        'ourselves', 'us', 'you', 'y','your', 'yours', 'yourself', 'yourselves', 
                        'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'sunday', 
       					'jan', 'january', 'feb', 'feburary', 'mar', 'march', 'april', 'may', 'june',
        				'july', 'aug', 'augest', 'sep', 'september', 'oct', 'october', 'nov', 'november', 'dec', 'december']


def nlp_noneed(tweets):
	tweet = []
	for i in tweets.tweet: 
	    word_tokens = nltk.word_tokenize(i) 
	   
	    filtered_sentence = [] 
	    
	    for w in word_tokens: 
	        if w not in noneed: 
	            filtered_sentence.append(w)
	    filtered_sentence = ' '.join(filtered_sentence)
	    tweet.append(filtered_sentence)
	tweets['tweet'] = tweet

	return tweets     

def nlp_lem(tweets):
	wnl = WordNetLemmatizer()
	tweet = []
	for data in tweets.tweet:
	    final= []
	    words = nltk.word_tokenize(data)
	    for word in words:
	        final.append(wnl.lemmatize(word))
	    final = ' '.join(final)
	    tweet.append(final)
	tweets['tweet'] = tweet

	return tweets	

def nlp_words(tweets):
	tweet = []
	for data in tweets.tweet:
	    final= []
	    words = nltk.word_tokenize(data)
	    for word in words:
	        if len(word) >= 3:
	            final.append(word)
	    final = ' '.join(final)
	    tweet.append(final)
	tweets['tweet'] = tweet

	return tweets

def nlp_country(tweets):
	country= []
	for c in pycountry.countries:
	    country.append(c.name.lower())
	tweet = []
	for i in tweets.tweet: 
	    word_tokens = nltk.word_tokenize(i) 
	    
	    filtered_sentence = [] 
	    
	    for w in word_tokens: 
	        if w not in country: 
	            filtered_sentence.append(w)
	    filtered_sentence = ' '.join(filtered_sentence)
	    tweet.append(filtered_sentence)
	tweets['tweet'] = tweet

	return tweets

def nlp_languages(tweets):
	lan= []
	for c in pycountry.languages:
	    lan.append(c.name.lower())
	tweet = []
	for i in tweets.tweet: 
	    word_tokens = nltk.word_tokenize(i) 
	    
	    filtered_sentence = [] 
	    
	    for w in word_tokens: 
	        if w not in lan: 
	            filtered_sentence.append(w)
	    filtered_sentence = ' '.join(filtered_sentence)
	    tweet.append(filtered_sentence)
	tweets['tweet'] = tweet

	return tweets

def nlp_drop(tweets):
    tweets['tweet'].replace(r'^\s*$', np.nan, regex=True, inplace=True)
    tweets = tweets.dropna().reset_index()
    
    return tweets

def nlp_clean(tweets):
	tweets = nlp_noneed(tweets)
	tweets = nlp_lem(tweets)
	tweets = nlp_words(tweets)
	tweets = nlp_country(tweets)
	tweets = nlp_languages(tweets)
	tweets = nlp_drop(tweets)

	return tweets