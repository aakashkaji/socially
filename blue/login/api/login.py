from flask import Flask
from pymongo import MongoClient
import hashlib
from flask import jsonify
from flask import request
import jwt
client = MongoClient('localhost', 27017)
db = client.mydb
collection = db.user.find()
for i in collection:
    print(i)

app = Flask(__name__)


def create_web_tokens():
    import jwt
    web_encode=jwt.encode({'key':'payload','key2':'value2'},'secret', algorithm= 'HS256')
    print(web_encode)
    web_decode=jwt.decode(web_encode,'secret', algorithms=['HS256'])
    print(web_decode)

# Token generations in python3
def create_jwt_token(**kwargs):
    web_encode=jwt.encode(kwargs,'secret',algorithm= 'HS256').decode()
    return web_encode



def auth(u,password):
    password=hashlib.md5(password.encode()).hexdigest()
    cl=db.user.find({"email" : u})
    for data in cl:
        user=data['email']
        passw=data['passw']
        if u == user and password == passw:
            #create tokens using user_name and password
            json_token=create_jwt_token(user_name=user,password=passw)
            return {'tokens':json_token}
        else:
            return {'user':'Invalid'}



@app.route("/user_login", methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        user_name = request.json.get('user_name')
        password = request.json.get('password')
        response=auth(user_name,password)


    return jsonify(response)

@app.route("/getdata")
def getdata():
    data=[]
    collection = db.user.find({"email":'aakash@gmail.com'},{"email":1,"passw":1,"_id":0})
    for i in collection:
        data.append(i)
    return jsonify(data)
@app.route("/value")
def value():
    return 'aaaaaaaaaa kadatakakkak'




app.run(debug=True)



