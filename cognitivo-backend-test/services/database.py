import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
engine = create_engine(os.environ['DATABASE_URI'])


def save_dataframe(frame, table, timestamp):
    with_saved_at = frame.assign(saved_at=[timestamp] * len(frame.index))
    with_saved_at.to_sql(table, con=engine, if_exists='append')
