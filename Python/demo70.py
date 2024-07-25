# Inheritence
class Base:
    def __init__(self):
        try:
            self.i = 10
            self._a = 3.14
            self.__s = "Hello"  # _Base__s
        except Exception as e:
            print("Base constructor error : ", e)

    def show(self):
        try:
            print(f"Base: {self.i}, {self._a}, {self.__s}")
        except Exception as e:
            print("Base.show error : ", e)


class Derived(Base):
    def __init__(self):
        try:
            super().__init__()
            self.i = 100
            self._a = 31.44
            self.__s = "Good Morning"
            
            self.j = 20
            self._b = 6.28
            self.__ss = "Hey"
        except Exception as e:
            print("Derived constructor error : ", e)
    
    def show(self):
        try:
            super().show()
            print(f"Derived: {self.i}, {self._a}, {self.__s}")
            print(f"Derived: {self.j}, {self._b}, {self.__ss}")
        except Exception as e:
            print("Derived.show() error : ", e)
            

def main(*args):
    try:
        b = Base()
        b.show()
        print("i = ", b.i)      # public
        print("a = ", b._a)     # protected
        # print(b.__s)    # private  Cause Error 
        print()
        
        d = Derived()
        d.show()
        print("j = ", d.j)      # public
        print("b = ", d._b)     # protected
        # print(d.__ss)   # private Cause Error 
        print()
        
        print(isinstance(b, Base))
        print(isinstance(b, Derived))
        print(isinstance(d, Base))
        print(isinstance(d, Derived))
        print()
        
        print(issubclass(Base, Derived))
        print(issubclass(Derived, Base))
        print(issubclass(Base, object))
        print(issubclass(Derived, object))
        print()
        
        print("object: ", dir(object)); print()
        print("Base: ", dir(Base)); print()
        print("Derived: ", dir(Derived)); print()
    
    except Exception as e: 
        print("main error : ", e)




if __name__ == "__main__":
    main()

