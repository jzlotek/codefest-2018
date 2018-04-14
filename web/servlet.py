from flask import Flask, request, send_from_directory, render_template, send_file, url_for, redirect
import json

app = Flask(__name__, static_url_path='')


@app.route("/test")
def my_webservice():
    return bytes('{"test": true}', encoding="UTF-8")


@app.route('/')
def ind():
    return redirect('/index.html')


@app.route('/<path:path>')
def index(path):
    return url_for('', path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
