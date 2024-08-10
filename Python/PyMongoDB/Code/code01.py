import pymongo as pm

myclient = pm.MongoClient("mongodb://localhost:27027/")
mydb = myclient["mydatabase"]
print(myclient.list_database_names())


