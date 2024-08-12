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
        
        myresult = mycol.find().limit(5)
        for x in myresult:
            print(x)
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()
