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
        
        query = """
        SELECT * FROM products;
        """
        mycursor.execute(query)
        table = mycursor.fetchall()
        for tb in table:
            print(tb)
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()
    
    
if __name__ == "__main__":
    main()


