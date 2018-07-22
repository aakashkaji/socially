# this is just for tutorials not used any kind of productions

from flask import Flask, request, jsonify, Response
from flask import json

app = Flask(__name__)

lingual = [{'name': 'python'}, {'name': 'javascript'}]


@app.route('/index', methods=['GET'])
def index():
    return jsonify({'message': 'Work success mmmmfully'})


@app.route('/language', methods=['GET'])
def language():
    return jsonify({'key': lingual})


@app.route('/added', methods=['POST'])
def add():
    data = request.get_json(force=True)
    l = {'nam': data['name']}
    lingual.append(l)

    return jsonify({'lang': lingual})


app.run(debug=True)
