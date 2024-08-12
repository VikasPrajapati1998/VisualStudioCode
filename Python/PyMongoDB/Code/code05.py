def main(*args):
    try:
        import pymongo as pm
        
        myclient = pm.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb['customers']
        
        # find all the collection
        print("---------------------------------------------------")
        for x in mycol.find():
            print(x)
        print()
        
        # find some specific fields
        print("---------------------------------------------------")
        for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
            print(x)
        print()
        
        print("--------------------------------------------------")
        for x in mycol.find({}, {"_id": 0, "address": 1}):
            print(x)
        print()
        
        # filter the result
        print("--------------------------------------------------")
        myquery = {"address": "Park Lane 38"}
        
        mydoc = mycol.find(myquery)
        for x in mydoc:
            print(x)
        print()
        
        # sort the result
            # ascending order
        print("------------------------------------------------")
        mydoc = mycol.find({}, {"_id": 0, "name": 1}).sort("name", 1)
        for x in mydoc:
            print(x)
        print()
        
            # descending order
        print("------------------------------------------------")
        mydoc = mycol.find({}, {"_id": 0, "name": 1}).sort("name", -1)
        for x in mydoc:
            print(x)
        print()
        
        # delete document
            # delete one documents
        myquery = {"address": "Mountain 21"}
        mycol.delete_one(myquery)

            # delete many documents
        myquery = {"address": {"$regex": "^S"}}
        x = mycol.delete_many(myquery)
        print(x.deleted_count, "documents deleted.")
        
            # delete all documents in a collection
        
        x = mycol.delete_many({})
        print(x.deleted_count, "documents deleted.")
        print()

        
        # delete collection
        mycol.drop()
        
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()
