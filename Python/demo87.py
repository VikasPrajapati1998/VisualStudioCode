class Sample:
    def __init__(self, data):
        self.__data = data
        self.__len = len(data)
        self.__pos = 0
    
    def set_data(self, data):
        self.__data = data
        
    def get_data(self):
        self.__data = [int(x) for x in input("Enter a number : ").split()]
    
    def show_data(self):
        print(self.__data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__pos >= self.__len:
            raise StopIteration
        else:
            self.__value = self.__data[self.__pos]
            self.__pos += 1
            return self.__value

    

def main(*args):
    try:
        lst = [x*2 for x in range(1, 10)]
        s = Sample(lst)
        for x in s:
            print(x, end=", ")
        print()
        
        s.show_data()
        
    
    except ZeroDivisionError as zde:
        print("main erro zde : ", zde)
    
    except Exception as e:
        print("main error e : ", e)
    
    finally:
        print()
        print("Program End.")




if __name__ == "__main__":
    main()
