def main(*args):
    try:
        import pymongo as pm
        
        client = pm.MongoClient()
        print(client)
        
        client = pm.MongoClient("mongodb://localhost:27017")
        print(client)
        
        myclient = pm.MongoClient(
            host="localhost", 
            port=27017)
        
        print(myclient.list_database_names())
        mydb = myclient["arjundb"]
        
        print(mydb.list_collection_names())
        mycol = mydb["tutorial"]; print()
        
        data = mycol.find()
        for field in data:
            print(field)
            print()
        print()
        
        for field in mycol.find({}, {"_id": 0, "title": 1}):
            print(field)
            print()
        print()
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()
    


if __name__ == "__main__":
    main()
