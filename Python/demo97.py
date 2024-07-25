class Stack:
    def __init__(self, size):
        self.__size = size
        self.__arr = []
        self.__top = -1
    
    def push(self, n):
        if self.__top == self.__size:
            raise IndexError('Stack is full.')
        else:
            self.__top += 1
            self.__arr = self.__arr + [n]
    
    def pop(self):
        if self.__top == -1:
            raise IndexError('Stack is empty.')
        else:
            n = self.__arr[self.__top]
            self.__top -= 1
            return n
    
    def printall(self):
        print("[", self.__arr, "]")

# ================================================================================================
def main(*args):
    try:
        stack1 = Stack(5)
        
        try:
            stack1.push(10)
            n = stack1.pop()
            print(n)
            
            n = stack1.pop()
            print(n)
            
            stack1.push(20)
            stack1.push(30)
            stack1.push(40)
            stack1.push(50)
            stack1.push(60)
            stack1.printall()
            
            stack1.push(70)
            
        except IndexError as ie:
            print(ie.args)
    
    except Exception as e:
        print("main error : ", e)
        print(e.args)
# ================================================================================================


if __name__ == "__main__":
    main()


