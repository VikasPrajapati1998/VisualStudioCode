def main(*args):
    try:
        import mysql.connector
        
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Arjun@191198",
            database = "mydatabase"
        )
        mycursor = mydb.cursor()
        
        sql = """UPDATE customers SET address = "Canyon 123" WHERE address = "Valley 345";"""
        mycursor.execute(sql)
        mydb.commit()
        
        print(mycursor.rowcount, "record(s) affected")
        
        
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()

