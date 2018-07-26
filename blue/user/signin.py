'''import sys

print(sys.path)'''

from helper import Dbconnect, RedisDb, Token
from flask import Flask, jsonify, request, Blueprint, abort
import hashlib
from blue .user .permission import *
import logging  # this used for as logging

logging.basicConfig(filename='newfile.log', format='%(asctime)s - %(name)s -%(levelname)s- %(message)s', filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

m = Dbconnect('localhost', 27017)  # type: Dbconnect
redis = RedisDb('localhost', '6379')
conn = m.db_select()
user_blueprint = Blueprint('user', __name__)


def auth1(username=None, password=None):
    password = hashlib.md5(password.encode()).hexdigest()

    # password change into sha256 for security reason
    db_query = conn.user.find({'email': username})

    for data in db_query:
       username_name = data['email']
       password_name = data['passw']
       logging.debug(username_name)

    if username == username_name and password == password_name:

        # creates token and save in redis and return as response
        token = Token.token_create(uid=username_name)
        # store token in Redis database
        redis.redis_store_token(token, username_name)

        return {'token': token}
    else:
        return {'response': 'Not valid login and password !!'}


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        # user_name = request.json.get('user_name')
        # user_password = request.json.get('user_password')
        data = request.get_json(force=True)
        user_name = data['user_name']
        user_password = data['user_password']

        print(user_name, user_password)
        response = auth1(user_name, user_password)
        return jsonify({'response': response})
    else:
        return {'response': 'your method is not post'}


@user_blueprint.route('/fetch', methods=['GET'])
def get_data():
    result = []
    # firstly validate token and gives result
    print(dict(request.headers.items()))
    # get token from header
    token = request.headers.get('token')
    print(token)
    status = redis.redis_validate_token(token)
    if status:
        # query database
        cursor = conn.user.find({}, {"_id": 0})
        for data in cursor:
            result.append(data)
        return jsonify({'response': result})

    else:
        return abort(404)

#  This route is just for testing purpose


@user_blueprint.route('/test_user')
@check_permission('resource1')
def test():
    logging.debug('test routes success')
    return 'testing success'
