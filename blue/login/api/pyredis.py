import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0)

print(r.keys())
n='name'
print(r.get(n))


# assertion in python

# syntax assert<condition> <meaasage>


st = ''
try:
    assert (st==''), 'string contains null value'

    if str=='akki':
        print("aakakak")
    else:
        print("not checked")
except AssertionError:
    print("asseration error occuredd")