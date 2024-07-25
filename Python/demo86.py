# =======================================================================================================================
class Progression:
    def __init__(self, start=0):
        self._cur = start
    
    def __iter__(self):
        return self
    
    def advance(self):
        self._cur += 1
        
    def __next__(self):
        if self._cur is None:
            raise StopIteration
        else:
            data = self._cur
            self.advance()
            return data

    def display(self, n):
        print(' '.join(str(next(self)) for i in range(n)))
# =======================================================================================================================


# =======================================================================================================================
class AP(Progression):
    def __init__(self, start=0, step=1):
        super().__init__(start)
        self.__step = step
        
    def advance(self):
        self._cur += self.__step
# =======================================================================================================================


# =======================================================================================================================
class GP(Progression):
    def __init__(self, start=1, step=2):
        super().__init__(start)
        self.__step = step
    
    def advance(self):
        self._cur *= self.__step
# =======================================================================================================================


# =======================================================================================================================
class FP(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self.__prev = second - first
    
    def advance(self):
        self.__prev, self._cur = self._cur, (self.__prev + self._cur)
# =======================================================================================================================


# =======================================================================================================================
def main(*args):
    try:
        print("Default Progression: ")
        p = Progression()
        p.display(10)
        
        print("AP with step 5:", end=" ")
        a = AP(1, 5)
        a.display(10)
        
        print("GP with step 3:", end=" ")
        g = GP(1, 3)
        g.display(10)
        
        print("FP with step default:", end=" ")
        f = FP(4, 6)
        g.display(10)
    
    except Exception as e:
        print("main error : ", e)
# =======================================================================================================================



if __name__ == "__main__":
    main()

