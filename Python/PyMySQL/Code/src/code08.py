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
        
        query = """
        INSERT INTO customers (name, address) 
        VALUES (%s, %s);
        """
        value = [
            ("Paul", "Electronic City Phase 1"),
            ("Sean", "Developer Pur"),
            ("Marty", "New York"),
            ("Alex", "Toon Pur"),
            ('Peter', 'Lowstreet 4'),
            ('Amy', 'Apple st 652'),
            ('Hannah', 'Mountain 21'),
            ('Michael', 'Valley 345'),
            ('Sandy', 'Ocean blvd 2'),
            ('Betty', 'Green Grass 1'),
            ('Richard', 'Sky st 331'),
            ('Susan', 'One way 98'),
            ('Vicky', 'Yellow Garden 2'),
            ('Ben', 'Park Lane 38'),
            ('William', 'Central st 954'),
            ('Chuck', 'Main Road 989'),
            ('Viola', 'Sideway 1633'),
            ('Tony', 'California Area 56'),
            ('Chris Evan', 'Area 51'),
            ('Chris Hemsworth', 'Medagaskar')
            ]
        
        # mycursor.execute(query, value)
        mycursor.executemany(query, value)
        mydb.commit()
        
        print(mycursor.rowcount, "record inserted.")
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()


if __name__ == "__main__":
    main()
