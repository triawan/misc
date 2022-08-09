from pymongo import MongoClient
mongo_url = "mongodb://localhost:27017/"
mongo_db = MongoClient(mongo_url)

#create db
db = mongo_db["demo_db"]

#create collection
coll = db["Demo_Coll"]

#create document
coll.update_many({
    "usia": {"$gt": 35}
}, {
    "$set": {"hobi": "traveling"}
})