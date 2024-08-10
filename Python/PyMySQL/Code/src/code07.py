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
        
        query = """
        INSERT INTO customers (name, address) 
        VALUES (%s, %s);
        """
        value = ("Arjun", "Noida Sector 16")
        
        # mycursor.execute(query, value)
        mycursor.execute(query, value)
        mydb.commit()
        
        print(mycursor.rowcount, "record inserted.")
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()


if __name__ == "__main__":
    main()
