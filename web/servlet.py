from flask import Flask, request, send_from_directory, send_file, url_for,render_template
import json

app = Flask(__name__)


@app.route("/test")
def my_webservice():
    return bytes('{"test": true}', encoding="UTF-8")


@app.route('/')
def index():
    return render_template('index.html')
