class Date:
    def __init__(self, d:int=0, m:int=0, y:int=0) -> None:
        try:
            self.__day = d
            self.__month = m
            self.__year = y
        except Exception as e:
            print("Data Constructor error : ", e)
    
    def __eq__(self, other):
        try:
            if (self.__day == other.__day and self.__month == other.__month and self.__year == other.__year):
                return True
            else:
                return False
        except Exception as e:
            print("Data.__eq__ error : ", e)
    
    def show(self):
        try:
            print(f"{self.__day}/{self.__month}/{self.__year}")
        except Exception as e:
            print("Date.show error : ", e)
    
    
def main(*args):
    try:
        d1 = Date(2, 5, 2000)
        d1.show()
        d2 = Date(19, 11, 1998)
        d2.show()
        d3 = Date(18, 7, 1998)
        d3.show()
        d4 = Date(2, 5, 2000)
        d4.show()
        
        print(d1 == d4)
        print(d2 == d3)
        
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()

