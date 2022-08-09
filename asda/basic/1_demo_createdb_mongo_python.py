from pymongo import MongoClient
mongo_url = "mongodb://localhost:27017/"
mongo_db = MongoClient(mongo_url)

#create db
db = mongo_db["demo_db"]

#create collection
coll = db.create_collection("Demo_Coll")

#create document
data = dict()

data["nama"] = "ruhul"
data["usia"] = 30
data["hobi"] = ["makan", "ngoding", "membaca"]
data["nilai"] = [
    {
        "mk": "matematika",
        "skor": 100
    },
    {
        "mk": "bahasa inggris",
        "skor": 90
    },
    {
        "mk": "basis data",
        "skor": 80
    }
]
x = coll.insert_one(data).inserted_id