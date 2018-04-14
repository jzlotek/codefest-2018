from flask import Flask, request, send_from_directory, send_file
import json

app = Flask(__name__)


@app.route("/test")
def my_webservice():
    return bytes('{"test": true}', encoding="UTF-8")


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/<path:path>')
def index(path):
    return send_from_directory(path)
