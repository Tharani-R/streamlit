import twint
import pandas as pd


def scrap_tweet(username):
    c = twint.Config()
    c.Username = username
    c.Since = "2021-01-19"
    c.Pandas = True
    # Run
    twint.run.Search(c)
    tweet = twint.storage.panda.Tweets_df
    col = tweet[["date", "username", "tweet"]]
    return col