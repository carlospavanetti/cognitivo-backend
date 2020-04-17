import pandas as pd


def most_rated(frame, n=1):
    most_rated_id = frame.rating_count_tot.nlargest(n).index
    return frame.loc[most_rated_id]


data = pd.read_csv('data/AppleStore.csv')
news = data[data.prime_genre == 'News']
print(most_rated(news).track_name.values[0])

book = data[data.prime_genre == 'Book']
music = data[data.prime_genre == 'Music']
print(most_rated(book, 10).track_name.values)
print(most_rated(music, 10).track_name.values)
