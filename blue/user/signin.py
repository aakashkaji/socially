'''import sys

print(sys.path)'''
from helper import Dbconnect, RedisDb
from flask import Flask
from flask import request
from pymongo import MongoClient
import hashlib

mongo = Dbconnect('localhost', 27017)
redis = RedisDb('localhost', '6379')
collection = mongo.db_select('mydb')

app = Flask(__name__)

@app.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':
        user_name = request.json.get('user_name')
        user_password = request.json.get('user_password')
        response = {'response' : 'succes token'}


    else:
        return {'response' : 'Error occured'}


app.run(debug=True)