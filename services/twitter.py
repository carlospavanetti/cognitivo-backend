import os
from twitter import Twitter, OAuth


def client():
    CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
    ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
    ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

    return Twitter(
        auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
