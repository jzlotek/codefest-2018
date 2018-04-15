from flask import Flask, request, send_from_directory, render_template, send_file, url_for, redirect
import json
import hydraview.google_interface_resource

app = Flask(__name__, static_url_path='')


@app.route("/test")
def my_webservice():
    return bytes('{"test": true}', encoding="UTF-8")


@app.route("/getClosestHydrants")
def get():
    if request.args.get('address'):
        s = hydraview.google_interface_resource.get_gps_location(request.args.get('address'))[0]
        return bytes(s.toJSON(), encoding='UTF-8')
    else:
        return bytes('[]', encoding='UTF-8')


@app.route('/')
def ind():
    return redirect('/index.html')


@app.route('/<path:path>')
def index(path):
    return url_for('', path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
