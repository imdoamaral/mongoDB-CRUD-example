import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["sample_mflix"]
mycol = mydb["movies"]

mycol.insert_one({
    "title": "Dune: Part One",
    "genres": ["Action", "Adventure", "Drama"],
    "year": 2021,
    "imdbRating": 8.1,
    "directors": ["Denis Villeneuve"],
    "cast": ["Timothée Chalamet", "Rebecca Ferguson", "Zendaya"],
    "type": "movie"
})