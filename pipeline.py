import pandas as pd
from dotenv import load_dotenv
from services.twitter import client


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
