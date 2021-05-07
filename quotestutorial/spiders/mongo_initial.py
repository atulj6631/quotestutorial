import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["quotes"]

mydict = { "quotes": "John", "author": "this is a trial quote" }

x = mycol.insert_one(mydict)