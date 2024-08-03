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
        d1 = Date(19, 11, 1998)
        d1.printDate()
        
        d2 = Date()
        d2.set_date(18, 7, 1998)
        d2.printDate()
        
        d3 = Date(2, 5, 2000)
        d3.printDate()
        
        d4 = Date(-9, 4, 1992)
        d4.printDate()
        
        d5 = Date(8, -7, 1854)
        d5.printDate()
            
    
    except InvalidDate as id:
        print("Invalid Date Error : ", id)
    
    except Exception as e:
        print("main error : ", e)

# ###########################################################################################################



if __name__ == "__main__":
    main()

