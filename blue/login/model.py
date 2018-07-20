from pymongo import MongoClient
import pprint
from collections import OrderedDict
import hashlib

client = MongoClient('localhost', 27017)
db = client.mydb
collection = db.user

'''ls = []
for coll in collection.find():
    pprint.pprint(coll)
    ls.append(coll)
print(ls)'''

# insert data in db

def insert_user(dc):
    passw=dc['passw']
    passw=hashlib.md5(passw.encode()).hexdigest()
    dc['passw'] = passw
    collection.insert(dc)

# role decorator
def role_decorator(fun):
    pass
# authentication functions

def auth(u,password):
    password=hashlib.md5(password.encode()).hexdigest()
    cl=collection.find({"email" : u})
    for data in cl:
        user=data['email']
        passw=data['passw']
        if u == user and password == passw:
            print("success")
        else:
            print("Invalid !!")

    #print(user,passw)

dc = OrderedDict()
dc = {

    'name': 'manoj maurya',
    'email': 'manoj@gmail.com',
    'passw':'manoj1234',
    'mobile':'9810886510',
    'skills':['python','java','php','mysql',],
    'location':'noida'
}

# PyJWT tokens method define here
def create_web_tokens(**kwargs):
    import jwt
    web_encode=jwt.encode(kwargs,'secret', algorithm= 'HS256')
    print(type(web_encode))
    web_decode=jwt.decode(web_encode,'secret', algorithms=['HS256'])
    print(web_decode)


def create_jwt_token(**kwargs):
    print(kwargs)
    print(kwargs['user'])
    '''for key, value in kwargs.iteritems():
        print(key, '>', value)'''

create_jwt_token(user='aaka',password='akki123')
#insert_user(dc)
#auth('aakash@gmail.com','12345')
create_web_tokens(user='aakash',password='akki123')


