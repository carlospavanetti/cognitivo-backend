import pandas as pd

data = pd.read_csv('data/AppleStore.csv')
news = data[data.prime_genre == 'News']
most_rated_id = news.rating_count_tot.idxmax()
most_rated = news.loc[most_rated_id]
print(most_rated.track_name)
