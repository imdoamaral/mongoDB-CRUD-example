import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["sample_mflix"]
mycol = mydb["movies"]

myquery = { "title": "Dune: Part One" }

mycol.delete_one(myquery)