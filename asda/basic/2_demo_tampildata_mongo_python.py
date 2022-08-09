from pymongo import MongoClient
mongodbClient = "mongodb://localhost:27017/"
mongo_db = MongoClient(mongodbClient)
if mongodbClient:
    db = mongo_db["demo_db"]
    coll = db.get_collection("Demo_Coll")
    isidata = list(coll.find())
    for data in isidata:
        print(" nama: {},\n usia: {},\n hobi: {},\n nilai: {}".format(data["nama"], data["usia"], data["hobi"], data["nilai"]))
else:
    print("kode program tidak terhubung ke database")