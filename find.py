import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["sample_mflix"]
mycol = mydb["movies"]

for x in mycol.find():
    print(x)
