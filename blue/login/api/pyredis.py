import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0)

print(r.keys())
n= 'name'
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

# this function is used to store a complete dictionary into redis db as string
admin1 = {

    "key2": "POST",  # create operation performed
    "key3": "PUT",  # update operation performed
    "key4": "DELETE"  # delete operation performed

}
r.set('aakash',admin1)
def dict_redis():

    dict1 = {
        "resource1": {

            "GET": 1,
            "POST": 1
        },
        "resource2": {
            "GET": 1,
            "POST": 0
        }

    }
    r.set('akki',dict1)
    v = str(dict1)
    print(v)
    r.set('dict', v)

    print(type(v))

    c = eval(v)
    print(c)
    print(type(c))


p=r.get('akki').decode()
print(p)
print(type(p))