import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

def tweetLevel_vectorizer():
    pickle_in = open("vectorizer.pkl","rb")
    vectorizer = pickle.load(pickle_in)

    return vectorizer

def tweetLevel_prediction():
    pickle_in = open("prediction.pkl","rb")
    prediction = pickle.load(pickle_in)
    

    return prediction

def tweetLevel(tweets):
    vectorizer = tweetLevel_vectorizer()
    prediction = tweetLevel_prediction()
    input_data = vectorizer.transform(tweets.tweet)
    predict = prediction.predict(input_data)

    tweets['Class'] = predict

    return tweets






