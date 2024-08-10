def main(*args):
    try:
        import mysql.connector
        
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Arjun@191198",
        )

        mycursor = mydb.cursor()
        # mycursor.execute("CREATE DATABASE mydatabase;")
        mycursor.execute("SHOW DATABASES;")
        for db in mycursor:
            print(*db)
        print()
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()


if __name__ == "__main__":
    main()
