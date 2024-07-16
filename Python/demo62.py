import sys

class Fruit :
    count = 0
    
    def __init__(self, name:str='', size:int=0, color:str='') -> None:
        try:
            self.__name = name
            self.__size = size
            self.__color = color
            Fruit.count += 1
        
        except Exception as e:
            print("Fruit Constructor error : ", e)
    
    
    def show(self) -> None:
        try:
            print(f"{self.__name}, {self.__size}kg., {self.__color} color.")
        
        except Exception as e:
            print("Fruit.show error : ", e)
    
    
    def display(self) -> None:
        try:
            print("Total number of fruits : ", Fruit.count); print()
        
        except Exception as e:
            print("Fruit.display error : ", e)
    
    def __del__(self) -> None:
        try:
            del self.__name
            del self.__size
            del self.__color
        
        except Exception as e:
            print("Fruit Destructor error : ", e)
    
    
def main(*args):
    try:
        f1 = Fruit('Banana', 2, 'Yellow')
        f1.show()
        f1.display()
        
        f2 = Fruit('Apple', 5, 'Red')
        f2.show()
        f2.display()
        
        f3 = Fruit('Watermelone', 7, 'Green')
        f3.show()
        f3.display()
        
        f4 = Fruit('Blackberry', 3, 'Dark Blue')
        f4.show()
        f4.display()
        
        f5 = Fruit('Orange', 4, 'Orange')
        f5.show()
        f5.display()
        
        print()
        print(vars()); print()
        print(dir()); print()
        print("---------------------------------------------------------------------------------------------------")
        
        print(vars(Fruit)); print()
        print(dir(Fruit)); print()
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()


