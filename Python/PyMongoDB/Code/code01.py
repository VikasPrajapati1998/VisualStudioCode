
def main(*args):
    try:
        import pymongo as pm

        myclient = pm.MongoClient("mongodb://localhost:27017/")

        # database
        mydb = myclient["mydatabase"]

        print(myclient.list_database_names())  # list of databases
            # list of databases
        dblist = myclient.list_database_names()
        if "mydatabase" in dblist:
            print("The database exists.")
        
        # collection
        mycol = mydb["mycollection"]
        print(mydb.list_collection_names())  # list of collections
            # list of collections
        collist = mydb.list_collection_names()
        if "mycollection" in collist:
            print("The collection exists")
        
        # document
        mydoc = {"name": "John",
                 "address": "Highway 37",
                 "country": "USA"}
        field = mycol.insert_one(mydoc)
        print(field.inserted_id)
        
    
    except Exception as e:
        print("main error : ", e)

    finally:
        print()


if __name__ == "__main__":
    main()



