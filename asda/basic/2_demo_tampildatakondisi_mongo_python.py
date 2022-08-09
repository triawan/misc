from pymongo import MongoClient
mongo_url = "mongodb://localhost:27017/"
mongo_db = MongoClient(mongo_url)

#create db
db = mongo_db["demo_db"]

#create collection
coll = db["Demo_Coll"]

#query tampil data usia kurang dari 35
query = coll.find({"usia": {"$lt": 35}})

print("Data pelajar yang memiliki usia dibawah 35 adalah: ")
for data in query:
    print(data)