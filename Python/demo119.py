import json


# ============================================================================================================
class InvalidDate(Exception):
    def __init__(self, day:int, month:int, year:int):
        self.__day = day
        self.__month = month
        self.__year = year
        
    def get_details(self):
        return f"{self.__day}/{self.__month}/{self.__year}"


# ===========================================================================================================
def encoder_date(date):
    if isinstance(date, Date):
        return (date.get_day(), date.get_month(), date.get_year())
    else:
        raise TypeError("Date object is not JSON serializable.")


# ===========================================================================================================
class Date:
    def __init__(self, day:int=1, month:int=1, year:int=1000):
        if (1 <= day <= 31) and (1 <= month <= 12) and (1000 <= year <= 9999):
            self.__day = day
            self.__month = month
            self.__year = year
        else:
            raise InvalidDate(day, month, year)
    
    def set_date(self, day:int=1, month:int=1, year:int=1000):
        if (1 <= day <= 31) and (1 <= month <= 12) and (1000 <= year <= 9999):
            self.__day = day
            self.__month = month
            self.__year = year
        else:
            raise InvalidDate(day, month, year)
    
    def get_date(self):
        self.__day = int(input("Enter day: "))
        self.__month = int(input("Enter month: "))
        self.__year = int(input("Enter year: "))
        Date.__init__(self.__day, self.__month, self.__year)
        
    def get_day(self):
        return self.__day
    def get_month(self):
        return self.__month
    def get_year(self):
        return self.__year
        
    def __str__(self):
        if 1 <= self.__day <= 9 and 1 <= self.__month <= 9:
            return f"0{self.__day}/0{self.__month}/{self.__year}"
        elif 1 <= self.__day <= 9 and self.__month >= 10:
            return f"0{self.__day}/{self.__month}/{self.__year}"
        elif self.__day >= 10 and 1 <= self.__month <= 9:
            return f"{self.__day}/0{self.__month}/{self.__year}"
        else:
            return f"{self.__day}/{self.__month}/{self.__year}"
    
    def printDate(self):
        if 1 <= self.__day <= 9 and 1 <= self.__month <= 9:
            print(f"0{self.__day}/0{self.__month}/{self.__year}")
        elif 1 <= self.__day <= 9 and self.__month >= 10:
            print(f"0{self.__day}/{self.__month}/{self.__year}")
        elif self.__day >= 10 and 1 <= self.__month <= 9:
            print(f"{self.__day}/0{self.__month}/{self.__year}")
        else:
            print(f"{self.__day}/{self.__month}/{self.__year}")

# ===========================================================================================================


# ###########################################################################################################
def main(*args):
    try:
        lst_date = [Date(11, 11, 2000),
                    Date(19, 11, 1998),
                    Date(2, 5, 2000),
                    Date(18, 7, 1998),
                    Date(21, 11, 2002),
                    Date(4, 4, 2000),
                    Date(25, 12, 2024),
                    Date(9, 7, 2020),
                    Date(17, 1, 2016),
                    Date(13, 7, 2013)]
        
        for date in lst_date:
            date.printDate()
        
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        with open(path+"text16.txt", "w") as file:
            for date in lst_date:
                json.dump(date, file, default=encoder_date)
                file.write('\n')
            
    
    except InvalidDate as id:
        print("Invalid Date Error : ", id)
    
    except Exception as e:
        print("main error : ", e)
        print(e.__annotations__())
    
    finally:
        print()

# ###########################################################################################################




if __name__ == "__main__":
    main()
