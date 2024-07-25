# Inheriting From collections.abc.Iterator
'''
The collections.abc module includes an abstract base class (ABC) called Iterator.

'''
from collections.abc import Iterator

class SequenceIterator(Iterator):
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0
    
    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration


def main(*args):
    try:
        # lst = [float(x) for x in input("Enter list : ").split(" ")]
        lst = [float(format((x*9)/7, ".2f")) for x in range(1, 10)]
        seq = SequenceIterator(lst)
        iter1 = seq.__iter__()
        for number in iter1:
            print(number, end=", ")
        print()
            

        # Creating Generator Iterators
        def sequence_generator(sequence):
            for item in sequence:
                yield item
        
        seq = sequence_generator(lst)
        for x in seq:
            print(x, end=", ")
        print()
        
        for number in sequence_generator(lst):
            print(number, end=", ")
        print()
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()
