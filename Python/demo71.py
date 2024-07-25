class Product:
    def __init__(self):
        self.__title = input("Enter title: ")
        self.__price = input("Enter price: ")
    
    def display_data(self):
        print(self.__title, self.__price)
    

class Sales:
    def __init__(self):
        self.__sales_figures = [int(x) for x in input("Enter sales fig: ").split()]
    
    def display_data(self):
        print(self.__sales_figures)


class HardwareItem(Product, Sales):
    def __init__(self):
        Product.__init__(self)
        Sales.__init__(self)
        self.__category = input("Enter category: ")
        self.__oem = input("Enter oem: ")
    
    def display_data(self):
        Product.display_data(self)
        Sales.display_data(self)
        print(self.__category, self.__oem)


# #################################################################################
def main(*args):
    try:
        print(dir(object))
        print(dir(object).__class__)
        hw1 = HardwareItem()
        hw1.display_data()
        
        hw2 = HardwareItem()
        hw2.display_data()
    
    except Exception as e:
        print("main error : ", e)
# #################################################################################

if __name__ == "__main__":
    main()

