from flask import Flask, jsonify, request
from pymongo import MongoClient
import hashlib
import redis
import jwt

client = MongoClient('localhost', 27017)
db = client.mydb
collection = db.user.find()
for i in collection:
    print(i)

app = Flask(__name__)


# Here created token store in redis and check and validate token during request.


class RedisDb:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.r = redis.StrictRedis(host=self.host, port=self.port, db=0)

    def store_token(self, token, uid):
        key = hashlib.md5(uid.encode()).hexdigest()
        self.r.set(key, token)
        print('token stores in redis')

    def validate_token(self, token):
        # get uid from tokens and convert into md5 and get keys of token
        token_decode = jwt.decode(token, 'secret', algorithms=['HS256'])
        print(token_decode)
        values = token_decode['uid']

        # uid convert into md5 for making keys of redis
        key = hashlib.md5(values.encode()).hexdigest()

        original_token = self.r.get(key)
        if original_token is not None:
            # code for verify tokens here
            return {'user': 'token verified'}
        else:
            return {'user': 'not validate token not match'}


obj = RedisDb('localhost', '6379')


def create_web_tokens():
    web_encode = jwt.encode({'key': 'payload', 'key2': 'value2'}, 'secret', algorithm='HS256')
    print(web_encode)
    web_decode = jwt.decode(web_encode, 'secret', algorithms=['HS256'])
    print(web_decode)


# Token generations in python3
def create_jwt_token(**kwargs):
    web_encode = jwt.encode(kwargs, 'secret', algorithm='HS256').decode()
    # store token in redis database
    uid = kwargs['uid']
    obj.store_token(web_encode, uid)
    return web_encode


def auth(u, password):
    password = hashlib.md5(password.encode()).hexdigest()
    cl = db.user.find({"email": u})
    for data in cl:
        user = data['email']
        passw = data['passw']
        if u == user and password == passw:

            # create tokens using user_name and password

            json_token = create_jwt_token(uid=user, password=passw)
            return {'tokens': json_token}
        else:
            return {'user': 'Invalid'}


@app.route("/user_login", methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        user_name = request.json.get('user_name')
        password = request.json.get('password')
        response = auth(user_name, password)

    return jsonify(response)


@app.route("/getdata")
def getdata():
    data = []
    collection = db.user.find({"email": 'aakash@gmail.com'}, {"email": 1, "passw": 1, "_id": 0})
    for i in collection:
        data.append(i)
    return jsonify(data)


app.run(debug=True)
