from blue.user.helper import Dbconnect, RedisDb

mongo = Dbconnect('localhost', 27017)
redis = RedisDb('localhost', '6379')


print(mongo.check_something())

print(redis.do_some())