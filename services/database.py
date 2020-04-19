from sqlalchemy import create_engine

engine = create_engine('sqlite:///output/database.db')


def save_dataframe(frame, table, timestamp):
    with_saved_at = frame.assign(saved_at=[timestamp] * len(frame.index))
    with_saved_at.to_sql(table, con=engine, if_exists='append')
