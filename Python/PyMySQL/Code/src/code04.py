import mysql.connector
import numpy as np
import pandas as pd


def main() -> None:
    """
    Main function, Program execution start from here.
    Update the table values
    :parameter: None
    :return: N
    :parameter:
        ConnectionFail: If Connection of mysql server fail to python.
        AnyError: If anything inappropriate happen.
    """
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Arjun@191198"
        )
        mycursor = mydb.cursor()
        print("List of Available Database : ")
        mycursor.execute("Show databases;")
        for db in mycursor:
            print(*db)

        print()
        db = input("Enter the database name which you want to use : ")
        showdata(db)

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Arjun@191198",
            database=f"{db}"
        )
        mycursor = mydb.cursor()
        createTable = """
                        CREATE TABLE Salary_Data(
                            ID INT AUTO_INCREMENT KEY,
                            Age DOUBLE(8, 1),
                            Gender VARCHAR(7),
                            Education_Level VARCHAR(50),
                            Job_Title VARCHAR(50),
                            Years_of_Experience DOUBLE(10, 2),
                            Salary DOUBLE(15, 3)
                        );
                    """
        mycursor.execute(createTable)
        mydb.commit()

        showdata(db)
        # -------------------------------------------------------------------------
        insertInto = """
                    INSERT INTO Salary_Data(
                        Age, Gender, Education_Level, Job_Title, Years_of_Experience, Salary) 
                        VALUES(%s, %s, %s, %s, %s, %s)
                    """
        df = pd.read_csv("../data/Salary_Data.csv")
        # columns names :
        # Age(float), Gender(str), Education Level(str), Job Title(str), Year of Experience(float), Salary(float)
        shape = df.shape[0]
        for x in range(0, shape):
            row = df.iloc[x, :]
            # print(row)
            age = float(row['Age'])
            gender = str(row['Gender'])
            el = str(row['Education Level'])
            jt = str(row['Job Title'])
            ye = float(row['Years of Experience'])
            salary = float(row['Salary'])
            insertValue = [(age, gender, el, jt, ye, salary)]
            mycursor.executemany(insertInto, insertValue)
            mydb.commit()

        showdata(db)

    except Exception as e:
        print(e)


def showdata(db: str) -> None:
    """
    Show the content of table.
    :parameter:
        db(str): Name of database
    :return: N
    :raises:
        ConnectionError: If connection fail to MySQL server.
        AnyError: If anything inappropriate happen.
    """
    print("---------------------------------------------------------")
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="admin#rohan@420",
            database=f"{db}"
        )
        mycursor = mydb.cursor()
        print()
        print("List of Available Tables : ")
        mycursor.execute("Show tables;")
        for tb in mycursor:
            print(*tb)

        print()
        table_name = input("Enter the name of table to see data(e to exit) : ")
        if table_name == "e":
            return
        mycursor.execute(f"SELECT * FROM {table_name};")
        table = mycursor.fetchall()
        for tb in table:
            print(tb)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()



"""
__author__: Arjun Prajapati
"""