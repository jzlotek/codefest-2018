from flask import Flask, request, send_from_directory, render_template, send_file, url_for, redirect
import json
import hydraview.google_interface_resource
from hydraview.quadtree_service import build_list, get_closest_to_point

app = Flask(__name__, static_url_path='')

hydrants = []

string = ""
with open('./hydraview/hydrants.json', 'r') as file:
    for line in file:
        string += line
hydrants = build_list(string)


def jsonify(li):
    j = "["
    for i, e in enumerate(li):
        if i < len(li) - 1:
            j += (str(e.toJSON()) + ',')
        else:
            j += str(e.toJSON())
    return j + "]"


@app.route("/getOutOfService")
def my_webservice():
    oos = []
    for hydrant in hydrants:
        if hydrant.OutOfService:
            oos.append(hydrant)

    return bytes(str(oos), encoding="UTF-8")


@app.route("/getClosestHydrants")
def get():
    if request.args.get('address'):
        s = hydraview.google_interface_resource.get_gps_location(request.args.get('address'))[0]
        if request.args.get('max'):
            closest = get_closest_to_point(hydrants, s, max_num=abs(request.args.get('max')))
        else:
            closest = get_closest_to_point(hydrants, s)

        return bytes(jsonify(closest), encoding='UTF-8')
    else:
        return bytes('[]', encoding='UTF-8')


@app.route('/')
def ind():
    return redirect('/index.html')


@app.route('/<path:path>')
def index(path):
    return url_for('', path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
