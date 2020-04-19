from services.twitter import client


class TweetsCount():
    def __init__(self, query):
        self._query = query
        self._api = client()

    def value(self):
        count = 0
        max_id = None
        while True:
            new_tweets = self._api.search(
                q=self._query, max_id=max_id, count=100)

            if not new_tweets:
                break
            count += len(new_tweets)
            max_id = new_tweets[-1].id - 1
        return count


def preprocessed_name(name):
    # clean_name = re.sub(r'(-|–|&|,|!|and|by)', '', name)
    limited_name = ' '.join(name.split()[:4])
    return limited_name


def with_tweets_citations_count(frame):
    citations = [TweetsCount(preprocessed_name(row.track_name)).value()
                 for _, row in frame.iterrows()]
    enriched = frame.assign(n_citacoes=citations)
    return enriched
