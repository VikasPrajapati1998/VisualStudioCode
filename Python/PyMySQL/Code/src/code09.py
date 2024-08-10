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
        
        # show tables
        mycursor.execute("SHOW tables;")
        for db in mycursor:
            print(*db)
        print()
        
        # fetch all record
        # query = "SELECT * FROM customers;"
        query = "SELECT id, name, address FROM customers;"
        mycursor.execute(query)
        table = mycursor.fetchall()
        for record in table:
            print(*record, sep=", ")
        print()
        
        # fetch one record
        query1 = "SELECT * FROM customers;"
        mycursor.execute(query1)
        record = mycursor.fetchone()
        print(record)
        
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()


if __name__ == "__main__":
    main()
