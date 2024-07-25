# Inheritance
# Base Class
class Base:
    def __init__(self):
        self._count = 0
    
    def display(self):
        print("Count = " + str(self._count))
    
    def incr(self):
        self._count += 1


# Derived Class
class Derived(Base):
    def __init__(self):
        super().__init__()
    
    def decr(self):
        self._count -= 1


# #########################################################################
def main(*args):
    try:
        d1 = Derived()
        d1.incr()
        d1.incr()
        d1.incr()
        d1.incr()
        d1.display()
        
        d1.decr()
        d1.display()
    
    except Exception as e:
        print("main error : ", e)


# #########################################################################


if __name__ == "__main__":
    main()

