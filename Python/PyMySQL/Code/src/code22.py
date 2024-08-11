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
        sql = """
        SELECT sellers.name AS Seller, products.name AS Customer
        FROM sellers INNER JOIN products ON sellers.id = products.id;
        """
        
        mycursor.execute(sql)
        table = mycursor.fetchall()
        
        for tb in table:
            print(tb)
        print()
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()




if __name__ == "__main__":
    main()
