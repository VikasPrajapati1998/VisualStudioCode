# Method Overloading
class Complex:
    def __init__(self, real:float=0.0, imag:float=0.0)-> None:
        """
        _summary_:
            Constructor of Complex Class.

        Args:
            real (float): real value of Complex Number.
            imag (float): imaginary value of Complex Number.
        
        Returns:
            None
        """
        try:
            self.__real = real
            self.__imag = imag
        except Exception as e:
            print("Complex Constructor error ", e)
    
    def show(self) -> None:
        """
        _summary_:
            Show method of Complex class. It will print the value.
        
        Args:
            None
        
        Returns:
            None
        """
        try:
            print(f"{self.__real} + {self.__imag}i")
        except Exception as e:
            print("Complex.show error ", e)
    
    # Arithmetic Operators Overloading
    def __add__(self, other):
        try:
            temp_real = float(format((self.__real + other.__real), ".2f"))
            temp_imag = float(format((self.__imag + other.__imag), ".2f"))
            return Complex(temp_real, temp_imag)
        except Exception as e:
            print("Complex.__add__ error : ", e)
    
    def __sub__(self, other):
        try:
            temp_real = float(format((self.__real - other.__real), ".2f"))
            temp_imag = float(format((self.__imag - other.__imag), ".2f"))
            return Complex(temp_real, temp_imag)
        except Exception as e:
            print("Complex.__sub__ error : ", e)
    
    def __mul__(self, other):
        try:
            temp_real = float(format((self.__real * other.__real), ".2f"))
            temp_imag = float(format((self.__imag * other.__imag), ".2f"))
            return Complex(temp_real, temp_imag)
        except Exception as e:
            print("Complex.__mul__ error : ", e)

    def __truediv__(self, other):
        try:
            temp_real = float(format((self.__real / other.__real), ".2f"))
            temp_imag = float(format((self.__imag / other.__imag), ".2f"))
            return Complex(temp_real, temp_imag)
        except Exception as e:
            print("Complex.__truediv__ error : ", e)
    
    def __mod__(self, other):
        try:
            temp_real = float(format((self.__real % other.__real), ".2f"))
            temp_imag = float(format((self.__imag % other.__imag), ".2f"))
            return Complex(temp_real, temp_imag)
        except Exception as e:
            print("Complex.__mod__ error : ", e)
    
    def __floordiv__(self, other):
        try:
            temp_real = float(format((self.__real // other.__real), ".2f"))
            temp_imag = float(format((self.__imag // other.__imag), ".2f"))
            return Complex(temp_real, temp_imag)
        except Exception as e:
            print("Complex.__floordiv__ error : ", e)
    
    def __pow__(self, other):
        try:
            temp_real = float(format((self.__real ** other.__real), ".2f"))
            temp_imag = float(format((self.__imag ** other.__imag), ".2f"))
            return Complex(temp_real, temp_imag)
        except Exception as e:
            print("Complex.__pow__ error : ", e)
    
    
    # Comparison Operators
    def __lt__(self, other):
        try:
            if (self.__real < other.__real) and (self.__imag < other.__imag):
                return True
            else:
                return False
        except Exception as e:
            print("Complex.__lt__ error : ", e)
    
    def __gt__(self, other):
        try:
            if (self.__real > other.__real) and (self.__imag > other.__imag):
                return True
            else:
                return False
        except Exception as e:
            print("Complex.__gt__ error : ", e)
    
    def __le__(self, other):
        try:
            if (self.__real <= other.__real) and (self.__imag <= other.__imag):
                return True
            else:
                return False
        except Exception as e:
            print("Complex.__le__ error : ", e)
    
    def __ge__(self, other):
        try:
            if (self.__real >= other.__real) and (self.__imag >= other.__imag):
                return True
            else:
                return False
        except Exception as e:
            print("Complex.__ge__ error : ", e)
    
    def __eq__(self, other):
        try:
            if (self.__real == other.__real) and (self.__imag == other.__imag):
                return True
            else:
                return False
        except Exception as e:
            print("Complex.__eq__ error : ", e)
            
    def __ne__(self, other):
        try:
            if (self.__real != other.__real) and (self.__imag != other.__imag):
                return True
            else:
                return False
        except Exception as e:
            print("Complex.__ne__ error : ", e)
    
    
    # Compound Assignment Operator
    def __iadd__(self, other):
        try:
            self.__real = float(format((self.__real + other.__real), ".2f"))
            self.__imag = float(format((self.__imag + other.__imag), ".2f"))
            return  self
        except Exception as e:
            print("Complex.__iadd__ error : ", e)
    
    def __isub__(self, other):
        try:
            self.__real = float(format((self.__real - other.__real), ".2f"))
            self.__imag = float(format((self.__imag - other.__imag), ".2f"))
            return  self
        except Exception as e:
            print("Complex.__isub__ error : ", e)
    
    def __imul__(self, other):
        try:
            self.__real = float(format((self.__real * other.__real), ".2f"))
            self.__imag = float(format((self.__imag * other.__imag), ".2f"))
            return  self
        except Exception as e:
            print("Complex.__iadd__ error : ", e)
    
    def __idiv__(self, other):
        try:
            self.__real = float(format((self.__real / other.__real), ".2f"))
            self.__imag = float(format((self.__imag / other.__imag), ".2f"))
            return  self
        except Exception as e:
            print("Complex.__iadd__ error : ", e)
    
    def __ifloordiv__(self, other):
        try:
            self.__real = float(format((self.__real // other.__real), ".2f"))
            self.__imag = float(format((self.__imag // other.__imag), ".2f"))
            return  self
        except Exception as e:
            print("Complex.__iadd__ error : ", e)
    
    def __imod__(self, other):
        try:
            self.__real = float(format((self.__real % other.__real), ".2f"))
            self.__imag = float(format((self.__imag % other.__imag), ".2f"))
            return  self
        except Exception as e:
            print("Complex.__iadd__ error : ", e)
    
    def __ipow__(self, other):
        try:
            self.__real = float(format((self.__real ** other.__real), ".2f"))
            self.__imag = float(format((self.__imag ** other.__imag), ".2f"))
            return  self
        except Exception as e:
            print("Complex.__iadd__ error : ", e)
    

    def __int__(self):
        try:
            return (int(self.__real))
        except Exception as e:
            print("Complex.__int__ error : ", e)
    
    def __float__(self):
        try:
            return (float(self.__real))
        except Exception as e:
            print("Complex.__float__ error : ", e)
    
    def __complex__(self):
        try:
            return (complex(self.__real, self.__imag))
        except Exception as e:
            print("Complex.__complex error : ", e)


    def __del__(self):
        del self.__real
        del self.__imag
        

# ####################################################################################################
def main(*args):
    """
    _summary_: 
        This is the main function of program. The program execution start from here.
    
    Args:
        args: Variable Length Positional Arguments
    
    Returns:
        None
    """
    try:
        # Arithmetic Operators --------------------------------------------------------------
        c1 = Complex(1.1, 0.1)
        print("c1 = ", end=''); c1.show()
        c2 = Complex(2.4, 1.2)
        print("c2 = ", end=''); c2.show()
        
        c3 = Complex()
        c3 = c1 + c2
        print("c3 = ", end=''); c3.show() 
        c4 = Complex()
        c4 = c1 + c2 + c3
        print("c4 = ", end=''); c4.show()
        
        c5 = Complex()
        c5 = c2 - c1
        print("c5 = ", end=''); c5.show()
        
        c6 = Complex()
        c6 = c1 * c2
        print("c6 = ", end=''); c6.show()
        # -----------------------------------------------------------------------------------
        
        # Comparison Operators --------------------------------------------------------------
        b1 = c4 > c5
        print(b1)
        
        b2 = c3 < c1
        print(b2)
        
        b3 = c3 >= c1
        print(b3)
        
        b4 = c6 <= c4
        print(b4)
        
        b5 = c1 != c2
        print(b5)
        # -----------------------------------------------------------------------------------
        
        # Compound Assignment Operators -----------------------------------------------------
        a1 = Complex(4.5, 1.2)
        print("a1 = ", end=''); a1.show()
        
        a2 = Complex(2.3, 9.0)
        print("a2 = ", end=''); a2.show()
        
        a1 += a2
        print("a1 = ", end=''); a1.show()
        
        a3 = Complex(5.6, 3.4)
        print("a3 = ", end=''); a3.show()
        
        a1 -= a3
        print("a1 = ", end=''); a1.show()
        
        a4 = Complex(4, 8)
        a2 **= a4
        print("a2 = ", end=''); a2.show()
        # -----------------------------------------------------------------------------------
        
        b1 = Complex(2.3, 0.7)
        b1.show()
        print(int(b1))
        print(float(b1))
        print(complex(b1))
        
        
    except Exception as e:
        print("main error : ", e)

# ####################################################################################################


if __name__ == "__main__":
    main()

