# iterator implementation
# ==================================================================
class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = float(format(self._sequence[self._index], '.2f'))
            self._index += 1
            return item
        else:
            raise StopIteration
    
    def iter(self):
        return self
    
    def next(self):
        if self._index < len(self._sequence):
            item = float(format(self._sequence[self._index], ".2f"))
            self._index += 1
            return item
        else:
            raise StopIteration
# ==================================================================

# ==================================================================
class SquireIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = float(format(self._sequence[self._index] ** 2, ".2f"))
            self._index += 1
            return item
        else:
            raise StopIteration
    
    def iter(self):
        return self
    
    def next(self):
        if self._index < len(self._sequence):
            item = float(format(self._sequence[self._index] ** 2, ".2f"))
            self._index += 1
            return item
        else:
            raise StopIteration
# ==================================================================

# ==================================================================
class MeanIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._sequence)-1:
            item = float(format((self._sequence[self._index] + self._sequence[self._index + 1]) / 2, '.2f'))
            self._index += 1
            return item
        else:
            raise StopIteration
    
    def iter(self):
        return self
    
    def next(self):
        if self._index < len(self._sequence)-1:
            item = float(format((self._sequence[self._index] + self._sequence[self._index + 1]) / 2, '.2f'))
            self._index += 1
            return item
        else:
            raise StopIteration
# ==================================================================


# ##################################################################
def main(*args):
    try:
        # Retrieve the next item
        lst = [float(x) for x in input("Enter List : ").split(" ")]
        
        iter = SequenceIterator(lst)
        print("List ", end=": ")
        for x in iter:
            print(x, end=", ")
        print() 
        
        seq = SquireIterator(lst)
        print("List ", end=": ")
        for x in seq:
            print(x, end=", ")
        print()
        
        seq = MeanIterator(lst)
        print("List ", end=": ")
        for x in seq:
            print(x, end=", ")
        print()
        
        seq_obj = SequenceIterator(lst)
        seq_iter = seq_obj.__iter__()
        print(seq_iter.__next__(), end=", ")
        print(seq_iter.__next__(), end=", ")
        print(seq_iter.__next__(), end=", ")
        print(seq_iter.__next__(), end=", ")
        print(seq_iter.__next__(), end=", ")
        print()
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()
        print("Program End....!")
        print()

# ##################################################################



if __name__ == "__main__":
    main()

