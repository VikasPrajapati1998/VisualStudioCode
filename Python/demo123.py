import json


def encode_date(d):
    if isinstance(d, Date):
        return {"__Date__": True, "day": d.get_day(), "month": d.get_month(), "year": d.get_year()}
    raise TypeError("Object of type Complex is not JSON serializable")

def decode_date(dct):
    if "__Date__" in dct:
        return Date(dct['day'], dct['month'], dct['year'])
    return dct


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
    def __init__(self, day:int=1, month:int=1, year:int=1000) -> None:
        if (1 <= day <= 31) and (1 <= month <= 12) and (1000 <= year <= 9999):
            self.__day = day
            self.__month = month
            self.__year = year
        else:
            raise InvalidDate(day, month, year)
    
    def set_date(self, day:int=1, month:int=1, year:int=1000) -> None:
        if (1 <= day <= 31) and (1 <= month <= 12) and (1000 <= year <= 9999):
            self.__day = day
            self.__month = month
            self.__year = year
        else:
            raise InvalidDate(day, month, year)
    
    def get_date(self) -> None:
        self.__day = int(input("Enter day: "))
        self.__month = int(input("Enter month: "))
        self.__year = int(input("Enter year: "))
        Date.__init__(self.__day, self.__month, self.__year)
        
    def __str__(self) -> str:
        if 1 <= self.__day <= 9 and 1 <= self.__month <= 9:
            return f"0{self.__day}/0{self.__month}/{self.__year}"
        elif 1 <= self.__day <= 9 and self.__month >= 10:
            return f"0{self.__day}/{self.__month}/{self.__year}"
        elif self.__day >= 10 and 1 <= self.__month <= 9:
            return f"{self.__day}/0{self.__month}/{self.__year}"
        else:
            return f"{self.__day}/{self.__month}/{self.__year}"
    
    def printDate(self) -> None:
        if 1 <= self.__day <= 9 and 1 <= self.__month <= 9:
            print(f"0{self.__day}/0{self.__month}/{self.__year}")
        elif 1 <= self.__day <= 9 and self.__month >= 10:
            print(f"0{self.__day}/{self.__month}/{self.__year}")
        elif self.__day >= 10 and 1 <= self.__month <= 9:
            print(f"{self.__day}/0{self.__month}/{self.__year}")
        else:
            print(f"{self.__day}/{self.__month}/{self.__year}")
    
    def __repr__(self) -> str:
        # return f"Date({self.__day}/{self.__month}/{self.__year})"
        if 1 <= self.__day <= 9 and 1 <= self.__month <= 9:
            return f"0{self.__day}/0{self.__month}/{self.__year}"
        elif 1 <= self.__day <= 9 and self.__month >= 10:
            return f"0{self.__day}/{self.__month}/{self.__year}"
        elif self.__day >= 10 and 1 <= self.__month <= 9:
            return f"{self.__day}/0{self.__month}/{self.__year}"
        else:
            return f"{self.__day}/{self.__month}/{self.__year}"
    
    def get_day(self) -> int:
        return self.__day
    def get_month(self) -> int:
        return self.__month
    def get_year(self) -> int:
        return self.__year

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
                    Date(15, 7, 2000),
                    Date(25, 12, 2024),
                    Date(13, 1, 1973)]
        
        # for date in lst_date:
        #     print(date)
        
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        with open(path+"text20.txt", "w") as file:
            json.dump(lst_date, file, default=encode_date)
        
        with open(path+"text20.txt", "r+") as file:
            file_content = json.load(file, object_hook=decode_date)
            print(file_content)
                
            
    
    except InvalidDate as id:
        print("Invalid Date Error : ", id)
    
    except Exception as e:
        print("main error : ", e)
        print(e.__annotations__())

# ###########################################################################################################



if __name__ == "__main__":
    main()
