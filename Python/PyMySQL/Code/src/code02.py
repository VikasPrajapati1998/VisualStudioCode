import mysql.connector


def main() -> None:
    """
    Create Table in Database.
        :param: None
        :return: N
        :raises:
            ConnectionError: If connection fail to mysql user.
            AnyError: If anything happen inappropriate.
    """
    try:
        # create table in database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="admin#rohan@420",
            database="arjundb"
        )
        mycursor = mydb.cursor()
        # mycursor.execute("DROP TABLE employee;")
        query = """
        CREATE TABLE employee(
        name varchar(50),
        sal int(20));       
        """
        mycursor.execute(query)

        mycursor.execute("SHOW TABLES")
        for tb in mycursor:
            print(*tb)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
    