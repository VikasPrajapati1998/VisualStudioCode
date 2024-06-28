# --------------------- Stack (LIFO) ---------------------
class stack :
    def __init__(self, size):
        self.__lst = []
        self.__pos = 0
        self.__size = size
    
    def push(self, value):
        if len(self.__lst) <= self.__size:
            self.__lst.append(value)
            self.__pos += 1
            print("Position = ", self.__pos)
        else:
            print("Stack is full.")
    
    def pop(self):
        if len(self.__lst) <= self.__size and self.__pos >= 0:
            self.__pos -= 1
            print("Position = ", self.__pos)
            return self.__lst.pop()
        else:
            print("Stack is empty.")
    
    def isEmpty(self):
        if bool(self.__lst) == False:
            return True
        else :
            return False
    
    def isFull(self):
        if len(self.__lst) == self.__size:
            return True
        else:
            return False
        
    
    def top(self):
        return self.__lst[0]
    
    def peek(self):
        return self.__lst[-1]
    
    def size(self):
        return self.__size
    
    def pos(self):
        return self.__pos - 1
    
    def display(self):
        print("Stack = ", self.__lst)

def main():
    s1 = stack(5)
    s1.push(2)
    s1.push(3)
    s1.push(4)
    s1.push(5)
    s1.push(6)
    s1.push(7)
    s1.push(8)
    s1.display()
    print(s1.pop())
    s1.display()
    print("Position = ", s1.pos())
    print(s1.isFull())
    print(s1.isEmpty())
    print("Size of Stack = ", s1.size())
    print()


if __name__ == "__main__":
    main()

