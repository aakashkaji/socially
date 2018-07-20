import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0)

print(r.keys())
n='name'
print(r.get(n))
