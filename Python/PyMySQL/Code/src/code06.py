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
        
        # create table
        query1 = '''
        CREATE TABLE customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            address VARCHAR(255)
        );
        '''
        mycursor.execute(query1)
        
        # alter table: add primary key into existing table.
        query2 = '''
        ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY;
        '''
        mycursor.execute(query2)
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()


if __name__ == "__main__":
    main()
