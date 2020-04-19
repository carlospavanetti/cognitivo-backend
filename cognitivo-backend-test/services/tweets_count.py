from services.twitter import client, ApiError


class TweetsCount():
    def __init__(self, query, api=None):
        self._query = query
        self._api = api or client()

    def value(self):
        queries = [self.__limited_name(), self.__app_suffixed()]
        return self.__unique_tweets_count(
            [self.__tweets(query) for query in queries])

    def __unique_tweets_count(self, array):
        tweet_ids = set()
        for chunk in array:
            for tweet in chunk:
                tweet_ids.add(tweet.id)
        return len(tweet_ids)

    def __limited_name(self, word_count=4):
        return ' '.join(self._query.split()[:word_count])

    def __app_suffixed(self):
        return self.__limited_name(2) + ' app'

    def __tweets(self, query):
        tweets, max_id = self.__partial(query)
        while max_id:
            news, max_id = self.__partial(query, max_id=max_id)
            tweets += news
        return tweets

    def __partial(self, query, max_id=None):
        tweets = []
        try:
            while True:
                new_tweets = self._api.search(
                    q=query, max_id=max_id, count=100)

                if not new_tweets:
                    break
                tweets += new_tweets
                max_id = new_tweets[-1].id - 1
            return [tweets, None]
        except ApiError:
            print('Timeout exception')
            return [tweets, max_id]


def with_tweets_citations_count(frame):
    api = client()
    count = [TweetsCount(row.track_name, api=api).value()
             for _, row in frame.iterrows()]
    enriched = frame.assign(n_citacoes=count)
    return enriched
