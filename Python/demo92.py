class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError("Pop from an empty stack.") from None
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __len__(self):
        return len(self._items)

# #######################################################################################
def main(*args):
    try:
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        s.push(6)
        
        s_iter = iter(s)
        print(s_iter)
        
        for value in s:
            print(value, end=", ")
    
    except Exception as e:
        print("main error : ", e)

# #######################################################################################




if __name__ == "__main__":
    main()

