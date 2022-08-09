from pymongo import MongoClient
mongo_url = "mongodb://localhost:27017/"
mongo_db = MongoClient(mongo_url)

#create db
db = mongo_db["demo_db"]

#create collection
coll = db["Demo_Coll"]

#create document
data = [
    {"nama": "sopian", "usia": 35, "hobi": "joging", "nilai": [{"mk": "ppki", "skor": 100}]},
    {"nama": "verry", "usia": 37, "hobi": "membaca", "nilai": [{"mk": "bahasa inggris", "skor": 90}]},
    {"nama": "fahmi", "usia": 33, "hobi": "berenang", "nilai": [{"mk": "bahasa indonesia", "skor": 90}]},
    {"nama": "irawan", "usia": 38, "hobi": "olahraga", "nilai": [{"mk": "ubiquitous computing", "skor": 100}]}
]

coll.insert_many(data)