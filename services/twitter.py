import os
from dotenv import load_dotenv
from tweepy import API, AppAuthHandler, TweepError


def client():
    load_dotenv()
    ACCESS_TOKEN = os.environ['TWITTER_CONSUMER_KEY']
    ACCESS_SECRET = os.environ['TWITTER_CONSUMER_SECRET']

    api = API(
        AppAuthHandler(ACCESS_TOKEN, ACCESS_SECRET),
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True,
        retry_count=5, retry_delay=10)

    if not api:
        raise Exception('Could not authenticate')
    return api


ApiError = TweepError
