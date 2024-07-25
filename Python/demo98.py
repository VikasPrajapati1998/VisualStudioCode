class QueueError(Exception):
    def __init__(self, msg, front, rear):
        self.__errmsg = msg + ' front = ' + str(front) + ', rear = ' + str(rear)
    
    def get_message(self):
        return self.__errmsg


class Queue:
    def __init__(self, size):
        self.__size = size
        self.__arr = []
        self.__front = self.__rear = -1
    
    def add_queue(self, item):
        if self.__rear == self.__size - 1:
            raise QueueError('Queue is full.', self.__front, self.__rear)
        else:
            self.__rear += 1
            self.__arr = self.__arr + [item]
        
            if self.__front == -1:
                self.__front = 0
    
    def delete_queue(self):
        if self.__front == -1:
            raise QueueError('Queue is empty.', self.__front, self.__rear)
        else:
            data = self.__arr[self.__front]
            if (self.__front == self.__rear):
                self.__front = self.__rear = -1
            else:
                self.__front += 1
            return data
    
    def printall(self):
        print(self.__arr)


# #################################################################################################################
def main(*args):
    try:
        queue = Queue(5)
        try:
            queue.add_queue(11)
            queue.add_queue(12)
            queue.add_queue(13)
            queue.add_queue(14)
            queue.add_queue(15)
            queue.printall()
            
            i = queue.delete_queue()
            print('Item deleted = ', i)
            
            i = queue.delete_queue()
            print('Item deleted = ', i)
            
            i = queue.delete_queue()
            print('Item deleted = ', i)
            
            i = queue.delete_queue()
            print('Item deleted = ', i)
            
            i = queue.delete_queue()
            print('Item deleted = ', i)
            
            i = queue.delete_queue()
            print('Item deleted = ', i)
            
            queue.printall()
        
        except QueueError as qe:
            print(qe.get_message())
    
    except Exception as e:
        print("main error : ", e)
# #################################################################################################################



if __name__ == "__main__":
    main()

