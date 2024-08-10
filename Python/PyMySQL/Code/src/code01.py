import mysql.connector


def main(*args):
    """
    :summary: Main function, Program start execution from here.
               Update the table values.
    :parameter: None
    :return: N
    :parameter:
        ConnectionFail: If connection of mysql server fail to python.
        AnyError: If anything inappropriate happen.
    """
    
    try:
        # check connection
        mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Arjun@191198",
                # database = f"{db}"
            )
        print("Connection Established.") if mydb else print("Connection Failed.")

        mycursor = mydb.cursor()  # create cursor
        
        print("List of Available Database: ")
        mycursor.execute("SHOW DATABASES")
        for db in mycursor:
            print(*db)
        print()
        
        db = input("Enter the name of database name which you want to use : ")
        # mydb = mysql.connector.connect(
        #         host = "localhost",
        #         user = "root",
        #         password = "Arjun@191198",
        #         database = f"{db}"
        #     )
        # print("Connection Established.") if mydb else print("Connection Failed.")

        # mycursor = mydb.cursor()  # create cursor
        
        showdata(db)
        
    
    except Exception as e:
        print("main error : ", e)



def showdata(db: str) -> None:
    """
    Summary: Show the content of table.
    Args:
        db (str): Name of database.
    Return: N
    Raises:
        ConnectionError: If connection fail to MySQL server.
        AnyError: If anything inappropriate happen.
    """
    print("----------------------------------------------------------------------------")
    try:
        # check connection
        mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Arjun@191198",
                database = f"{db}"
            )
        print("Connection Established.") if mydb else print("Connection Failed.")
        mycursor = mydb.cursor()  # create cursor
        
        print("List of Available Table: ")
        mycursor.execute("SHOW TABLES;")
        for tbl in mycursor:
            print(*tbl)
        print()
        
        table_name = input("Enter the name of table to see data: ")
        mycursor.execute(f"SELELCT * FROM {table_name};")
        table = mycursor.fetchall()
        for data in table:
            print(*data)
        print()
    
    except Exception as e:
        print("main error : ", e)








if __name__ == "__main__":
    main()


