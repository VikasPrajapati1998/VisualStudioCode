# Iterator
class AvgAdj:
    def __init__(self, data):
        try:
            self.__data = data
            self.__len = len(data)
            self.__first = 0
            self.__sec = 1
        except Exception as e:
            print("AvgAdj.__init__ error : ", e)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__sec >= self.__len:
            raise StopIteration
        
        self.__avg = (self.__data[self.__first] + self.__data[self.__sec]) / 2
        self.__first += 1
        self.__sec += 1
        return self.__avg


def main():
    try:
        lst = [x * 10 for x in range(1, 10)]
        col = AvgAdj(lst)
        for val in col:
            print(val, end=", ")
        print()
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()
