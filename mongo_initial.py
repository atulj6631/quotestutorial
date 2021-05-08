import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["quotes"]

mydict = [
        { "quotes": "Eliza", "author": "this is a trial quote for many inserts to mongodb" },
        { "quotes": "Dennis", "author": "this is a trial quote for many inserts to mongodb ver2" }
    ]

x = mycol.insert_many(mydict)