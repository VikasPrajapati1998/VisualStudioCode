# Generators
import sys

class Complex(object):
    def __init__(self, real:float=0.0, imag:float=0.0):
        try:
            self.__real = float(format(real, ".2f"))
            self.__imag = float(format(imag, ".2f"))
        except Exception as e:
            print("Complex.__init__ error : ", e)
    
    def set_data(self, real:float=0.0, imag:float=0.0):
        try:
            self.__real = float(format(real, ".2f"))
            self.__imag = float(format(imag, ".2f"))
        except Exception as e:
            print("Complex.set_data error : ", e)
    
    def get_data(self):
        try:
            self.__real = float(input("Enter real number : "))
            self.__real = float(format(self.__real, ".2f"))
            self.__imag = float(input("Enter imag number : "))
            self.__imag = float(format(self.__imag, ".2f"))
        except Exception as e:
            print("Complex.get_data error : ", e)
    
    def show_data(self):
        try:
            print(f"{self.__real} + {self.__imag}i")
        except Exception as e:
            print("Complex.show_data error : ", e)
    
    def __iter__(self):
        return self
    
    def __del__(self):
        try:
            del self.__real
            del self.__imag
        except Exception as e:
            print("Complex.__del__ error : ", e)


# ###################################################################################################
def main(*args):
    try:
        c = Complex(6.3, 2.4)
        c.show_data(); print()
        
        lst = [i*i for i in range(1, 20)]
        gen = (i*i for i in range(1, 20))
        
        print(lst)
        print(gen)
        print(list(gen)); print()
        
        print("list : ", sys.getsizeof(lst))
        print("generator : ", sys.getsizeof(gen))
    
    except Exception as e:
        print("main error : ", e)

# ###################################################################################################


if __name__ == "__main__":
    main()



