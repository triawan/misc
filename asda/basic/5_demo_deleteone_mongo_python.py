from pymongo import MongoClient
mongo_url = "mongodb://localhost:27017/"
mongo_db = MongoClient(mongo_url)

#create db
db = mongo_db["demo_db"]

#create collection
coll = db["Demo_Coll"]

#create document
query = {"usia": 33}
coll.delete_one(query)

for data in coll.find():
    print(data)