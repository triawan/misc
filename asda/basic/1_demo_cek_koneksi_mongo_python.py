from pymongo import MongoClient
mongodbClient = "mongodb://localhost:27017/"
if mongodbClient:
    print("kode program sudah terhubung ke mongodb")
else:
    print("kode program belum terhubung ke mongodb")