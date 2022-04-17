import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["sample_mflix"]
mycol = mydb["movies"]

myquery = {"title": "Dune: Part One"}
newvalues = {"$set": {
    "plot": "Dune tells the story of Paul Atreides, a brilliant gifted young man born into a great destiny beyond his understanding"
}}

mycol.update_one(myquery, newvalues)

for x in mycol.find():
    print(x)
