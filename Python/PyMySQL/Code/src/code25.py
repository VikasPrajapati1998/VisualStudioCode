def main(*args):
    try:
        import mysql.connector
        
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Arjun@191198",
            database = "demodb"
        )
        
        mycursor = mydb.cursor()
        
        sql = """
        select * from student limit 5;
        """
        mycursor.execute(sql)
        
        table = mycursor.fetchall()
        for record in table:
            print(record)
            print()
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()




if __name__ == "__main__":
    main()


