# ==================================================================
class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0
    
        
    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = float(format(self._sequence[self._index], ".2f"))
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

def main(*args):
    try:
        lst = [float(x) for x in input("Enter List : ").split(" ")]
        seq_obj = SequenceIterator(lst)
        seq_iter = iter(seq_obj)
        print(next(seq_iter))
        print(next(seq_iter))
        print(next(seq_iter))
        
        iter1 = SequenceIterator(lst)
        while True:
            try:
                # Retrieve the next item
                item = iter1.__next__()
            except StopIteration:
                break
            else:
                print(item)
        
    except Exception as e:
        print("main error : ", e)
        print(e.__annotations__)
    
    finally:
        print()
        print("Program Ends....!")
        print()



if __name__ == "__main__":
    main()

