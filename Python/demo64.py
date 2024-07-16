def print_it():
    print("Opener")


class Message:
    def __init__(self, msg=''):
        try:
            self.__msg = msg
        except Exception as e:
            print("Message Constructor error : ", e)
    
    def display(self, msg):
        try:
            print_it()
            print(msg)
        except Exception as e:
            print("Message.display error ", e)
    
    def show():
        try:
            print_it()
            print("Hello Show message.")
        except Exception as e:
            print("Message.show error : ", e)


def main(*args):
    try:
        print_it()
        m = Message()
        m.display("Good Morning")
        Message.show()
        
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()

