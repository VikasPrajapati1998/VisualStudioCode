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
    
    # def __iter__(self):
    #     return iter(self._items)

    # def __iter__(self):
    #     for item in self._items:
    #         yield item
    
    def __iter__(self):
        yield from self._items
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __len__(self):
        return len(self._items)



# #######################################################################################
def main(*args):
    try:
        s = Stack()
        s.push(10)
        s.push(12)
        s.push(32)
        s.push(47)
        s.push(35)
        s.push(85)
        
        s_iter = iter(s)
        print(s_iter)
        
        for value in s:
            print(value, end=", ")
    
    except Exception as e:
        print("main error : ", e)

# #######################################################################################




if __name__ == "__main__":
    main()

