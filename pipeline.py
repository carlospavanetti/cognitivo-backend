import pandas as pd


def most_rated(frame):
    most_rated_id = frame.rating_count_tot.idxmax()
    return frame.loc[most_rated_id]


data = pd.read_csv('data/AppleStore.csv')
news = data[data.prime_genre == 'News']
print(most_rated(news).track_name)

book = data[data.prime_genre == 'Book']
music = data[data.prime_genre == 'Music']
print(most_rated(book).track_name)
print(most_rated(music).track_name)
