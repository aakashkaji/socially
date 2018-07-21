
# We are using this file just for help
# Connection provides Redis db i.e toke store in db and get tokens from there

import redis
from pymongo import MongoClient
import hashlib
import jwt



class Dbconnect:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = MongoClient(self.host, self.port)

    def db_select(self,db_name):
        conn = self.client.db_name
        return conn

    def check_something(self):
        return 'mongo db work successfully'

class RedisDb:

    # this init method used as redis db
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.r = redis.StrictRedis(host=self.host, port=self.port, db=0) # r is used as connection to redis

    # This method used as store data in redis

    def redis_store_token(self, token, uid):

        # our key as md5 of uid and value is our token
        key = hashlib.md5(uid.encode()).hexdigest()
        self.r.set(key, token)
        print('token stores in redis')

    # This method used as get store data from redis

    def redis_validate_token(self,token):

        # From token extract uid and convert into md5 which becomes key of redis and get values
        token_decode = jwt.decode(token,'secret',algorithms=['HS256'])
        uid = token_decode['uid']

        # uid convert into md5 for making keys of redis
        key = hashlib.md5(uid.encode()).hexdigest()
        original_token = self.r.get(key)

        if original_token is not None:

            # This block used as validate tokens
            return {'response' : 'token verified'}

        else:
            return {'response' : 'token not verified !!'}

    def do_some(self):
        return 'Redis db run successfully'
