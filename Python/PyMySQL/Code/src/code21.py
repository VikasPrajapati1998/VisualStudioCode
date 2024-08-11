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
        CREATE TABLE sellers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            address VARCHAR(255),
            phone VARCHAR(14)
            );
        """
        mycursor.execute(sql)
        
        query = """
        INSERT INTO sellers (name, address, phone)
        VALUES (%s, %s, %s);
        """
        value = [
                ('John Doe', '123 Elm Street, Springfield, IL', '555-1234'),
                ('Jane Smith', '456 Oak Avenue, Springfield, IL', '555-5678'),
                ('Alice Johnson', '789 Pine Road, Springfield, IL', '555-9101'),
                ('Bob Brown', '101 Maple Lane, Springfield, IL', '555-1122'),
                ('Charlie Davis', '202 Birch Street, Springfield, IL', '555-3344'),
                ('Diana Evans', '303 Cedar Road, Springfield, IL', '555-5566'),
                ('Eric Wilson', '404 Walnut Avenue, Springfield, IL', '555-7788'),
                ('Fiona Clark', '505 Cherry Lane, Springfield, IL', '555-9900'),
                ('George Martinez', '606 Ash Street, Springfield, IL', '555-1234'),
                ('Hannah Lee', '707 Elm Street, Springfield, IL', '555-5678'),
                ('Ian White', '808 Oak Avenue, Springfield, IL', '555-9101'),
                ('Judy Adams', '909 Pine Road, Springfield, IL', '555-1122'),
                ('Kevin Miller', '1010 Maple Lane, Springfield, IL', '555-3344'),
                ('Laura Thompson', '1111 Birch Street, Springfield, IL', '555-5566'),
                ('Mike Roberts', '1212 Cedar Road, Springfield, IL', '555-7788'),
                ('Nina Harris', '1313 Walnut Avenue, Springfield, IL', '555-9900'),
                ('Oliver Scott', '1414 Cherry Lane, Springfield, IL', '555-1234'),
                ('Pamela Green', '1515 Ash Street, Springfield, IL', '555-5678'),
                ('Quincy Young', '1616 Elm Street, Springfield, IL', '555-9101'),
                ('Rachel Baker', '1717 Oak Avenue, Springfield, IL', '555-1122'),
                ('Steve Carter', '1818 Pine Road, Springfield, IL', '555-3344')
            ]
        
        mycursor.executemany(query, value)
        
        mydb.commit()
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()


