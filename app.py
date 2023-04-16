import pymongo

client = pymongo.MongoClient("mongodb://root:example@db:27017")

db = client["testdb"]
col = db["testcol"]

col.insert_one({"name": "Alice", "age": 30})

for doc in col.find():
    print(doc)
