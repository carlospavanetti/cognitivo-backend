from time import time
import pandas as pd
from services import database
from services.tweets_count import with_tweets_citations_count


def most_rated(frame, n=1):
    most_rated_id = frame.rating_count_tot.nlargest(n).index
    return frame.loc[most_rated_id]


def top_book_and_music_apps(frame):
    book_apps = frame[frame.prime_genre == 'Book']
    music_apps = frame[frame.prime_genre == 'Music']
    top_book = most_rated(book_apps, 10)
    top_music = most_rated(music_apps, 10)
    return pd.concat([top_book, top_music])


data = pd.read_csv('data/AppleStore.csv')
news = data[data.prime_genre == 'News']
print(most_rated(news).track_name.values[0])
selected_apps = top_book_and_music_apps(data)
enriched_data = with_tweets_citations_count(selected_apps)
output_data = enriched_data[
    ['id', 'track_name', 'n_citacoes', 'size_bytes', 'price', 'prime_genre']
]

timestamp = int(time())
filename = '{timestamp}_output'.format(timestamp=timestamp)
output_data.to_csv('output/{name}.csv'.format(name=filename), index=False)
output_data.to_json('output/{name}.json'.format(name=filename),
                    orient='records')
database.save_dataframe(output_data, 'top_rated_apps', timestamp)
