from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/top_rated_apps")
def top_rated_apps():
    return jsonify({})
