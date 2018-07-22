'''import sys

print(sys.path)'''

from helper import Dbconnect, RedisDb, Token
from flask import Flask, jsonify, request
import hashlib

m = Dbconnect('localhost', 27017)  # type: Dbconnect
redis = RedisDb('localhost', '6379')
conn = m.db_select()

app = Flask(__name__)


def auth1(username=None, password=None):
    password = hashlib.md5(password.encode()).hexdigest()

    # password change into sha256 for security reason
    db_query = conn.user.find({'email': username})

    for data in db_query:
       username_name = data['email']
       password_name = data['passw']

    if username == username_name and password == password_name:

        # creates token and save in redis and return as response
        token = Token.token_create(uid=username_name)
        # store token in Redis database
        redis.redis_store_token(token, username_name)

        return {'token': token}
    else:
        return {'response': 'Not valid login and password !!'}


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        #user_name = request.json.get('user_name')
        #user_password = request.json.get('user_password')
        data = request.get_json(force=True)
        user_name = data['user_name']
        user_password = data['user_password']

        print(user_name, user_password)
        response = auth1(user_name, user_password)
        return jsonify({'response': response})
    else:
        return {'response': 'your method is not post'}


@app.route('/fetch/<string:token>', methods=['GET'])
def get_data(token):

    print(token)
    result = []

    # firstly validate token and gives result
    status = redis.redis_validate_token(token)
    if status:
        cursor = conn.user.find({}, {"_id": 0})
        for data in cursor:
            result.append(data)
        print(result)
        return jsonify({'response': result})

        # query database
    else:
        return jsonify({'response': 'Sorry your token is invalid !!'})


    pass

app.run(debug=True)
