from flask import jsonify
from app.app_factory import create_app

app = create_app()
@app.route("/top_rated_apps")
def top_rated_apps():
    return jsonify({})
