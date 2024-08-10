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
        
        sql = """DELETE FROM customers WHERE address = 'Mountain 21';"""
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
        
        
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()
