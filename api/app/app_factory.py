import os
from dotenv import load_dotenv
from flask import Flask


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev'),
        DATABASE_URI=os.environ['DATABASE_URI']
    )
    return app
