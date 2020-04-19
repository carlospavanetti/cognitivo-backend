from flask import jsonify
from app.app_factory import create_app
from app.database import select_all

app = create_app()


@app.route("/top_rated_apps")
def top_rated_apps():
    result = select_all('top_rated_apps')
    data = [dict(row.items()) for row in result]
    return jsonify(data)
