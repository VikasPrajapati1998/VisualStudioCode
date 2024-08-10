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
        
        sql = """DELETE FROM customers WHERE address = %s;"""
        adr = ("Yellow Garden 2",)
        mycursor.execute(sql, adr)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
        
        
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()
