# We are using this file just for help
# Connection provides Redis db i.e toke store in db and get tokens from there

import redis
from pymongo import MongoClient
import hashlib
import jwt

""" This class is used for connecting mongo database and taking argument as host and port"""
class Dbconnect:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = MongoClient(self.host, self.port)

    def db_select(self):
        conn = self.client.mydb
        return conn


class RedisDb:

    # this init method used as redis db
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.r = redis.StrictRedis(host=self.host, port=self.port, db=0)  # r is used as connection to redis

    # This method used as store data in redis

    def redis_store_token(self, token, uid):
        """ it takes token in HS256 encryption and taking uid  and then stores
            in redis database here key is uid of md5 encryption and value
            is our token
        """

        # our key as md5 of uid and value is our token
        key = hashlib.md5(uid.encode()).hexdigest()
        self.r.set(key, token)

    def redis_validate_token(self, token):
        """ this method used to validate token and return true if success
            else return false value
        """

        original_token = ''
        # From token extract uid and convert into md5 which becomes key of redis and get values
        try:
            assert (token != ''), 'Token is null value'
            token_decode = jwt.decode(token, 'secret', algorithms=['HS256'])
            uid = token_decode['uid']

            # uid convert into md5 for making keys of redis
            key = hashlib.md5(uid.encode()).hexdigest()
            original_token = self.r.get(key).decode()

        except AssertionError:
            print('Assertion Error occur')

        if token == original_token:
            return True
        else:
            return False


class Token:
    @staticmethod
    def token_create(**kwargs):
        # only take uid field to create token of user

        web_token = jwt.encode(kwargs, 'secret', algorithm='HS256').decode()

        return web_token

    @staticmethod
    def decode_token(token):
        # this will returns payload of md5 i.e uid

        web_token = jwt.decode(token, 'secret', algorithms=['HS256'])
        uid = web_token['uid']

        return uid
