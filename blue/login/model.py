import pymongo

from pymongo import MongoClient
import pprint


client = MongoClient('localhost', 27017)

#Get the database mydb

db=client.mydb
collection=db.inventory           # inventory is collection name
ls=[]                            # get all document into a list
for coll in collection.find():
	pprint.pprint(coll)
	ls.append(coll)
print(ls)






