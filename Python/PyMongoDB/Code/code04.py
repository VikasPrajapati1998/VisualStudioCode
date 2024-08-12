def main(*args):
    try:
        import pymongo as pm
        
        myclient = pm.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb['customers']
        
        x = mycol.find_one()
        print(x)
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()
