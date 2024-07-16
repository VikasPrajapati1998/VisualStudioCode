class Complex:
    count = 0
    
    
    def __init__(self, real:float=0.0, imag:float=0.0) -> None:
        try:
            self.__real = real
            self.__imag = imag
            Complex.count += 1
        except Exception as e:
            print("Complex Constructor error : ", e)
    
    def __eq__(self, other) -> bool:
        try:
            if (self.__real == other.__real) and (self.__imag == other.__imag):
                return True
            else:
                return False
        except Exception as e:
            print("Complex __eq__ error : ", e)
    
    def __add__(self, other):
        try:
            temp__real = float(format((self.__real + other.__real), ".2f"))
            temp__imag = float(format((self.__imag + other.__imag), ".2f"))
            return Complex(temp__real, temp__imag)
        except Exception as e:
            print("Complex.__add__ error ", e)
    
    def show(self) -> None:
        try:
            print(f"({self.__real} + {self.__imag}i)")
        except Exception as e:
            print("Complex show error : ", e)
    
    @staticmethod
    def add_complex(c1, c2):
        try:
            temp__real = float(format((c1.__real + c2.__real), ".2f"))
            temp__imag = float(format((c1.__imag + c2.__imag), ".2f"))
            return Complex(temp__real, temp__imag)
        except Exception as e:
            print("staticmethod Complex.add_complex error ", e)
            
    
    @classmethod
    def print_count(cls):
        try:
            print(f"Object Count = {cls.count}, Class Variable Count = {Complex.count}")
        except Exception as e:
            print("classmethod Complex.print_count error ", e)



def main(*args):
    try:
        c1 = Complex(1.1, 0.2)
        c1.show()
        
        c2 = Complex(2.1, 0.4)
        c2.show()
        
        c3 = c1
        
        if c1 == c2:
            print("c1 and c2 are same.")
        else:
            print("c1 and c2 are different.")
        
        if type(c1) == type(c3):
            print("c1 and c3 are same.")
        else:
            print("c1 and c3 are different.")
        
        Complex.print_count()
        
        c4 = Complex()
        c4 = Complex.add_complex(c1, c2)
        print("c4 = ", end=''); c4.show()
        
        c5 = Complex(4.5, 3.2)
        print("c5 = ", end=''); c5.show()
        
        c6 = Complex(7.9, 2.3)
        print("c6 = ", end=''); c6.show()
        
        c7 = Complex()
        c7 = c5 + c6
        print("c7 = ", end=''); c7.show()
        
        c8 = Complex()
        c8 = c4 + c7
        print("c8 = ", end=''); c8.show()
        
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()

