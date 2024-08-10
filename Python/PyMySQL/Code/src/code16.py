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
        
        # sql = """DROP TABLE customers;"""
        sql = """DROP TABLE IF EXISTS customers;"""
        mycursor.execute(sql)
        mydb.commit()
        
        
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()

