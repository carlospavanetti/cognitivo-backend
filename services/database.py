from sqlalchemy import create_engine

engine = create_engine('sqlite:///output/database.db')


def save_dataframe(frame, table, timestamp):
    frame['saved_at'] = [timestamp] * len(frame.index)
    frame.to_sql(table, con=engine, if_exists='append')
