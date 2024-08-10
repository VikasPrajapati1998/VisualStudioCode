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
        
        sql = """SELECT * FROM customers WHERE address = %s;"""
        adr = ("Yellow Garden 2",)
        mycursor.execute(sql, adr)
        
        table = mycursor.fetchall()
        for record in table:
            print(record)
        
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()
