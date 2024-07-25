class Sample:
    count = 0
    def __init__(self, name="Arjun"):
        self.__name = name
        # count += 1  # act as a local variable
        Sample.count += 1
    
    def show_data(self):
        print("Name: ", self.__name)
    
    @staticmethod
    def print_count():
        print(Sample.count)
        # print(self.__name) # error 
    
    @classmethod
    def show_count(cls):
        print(cls.count)
        # print(self.__name) # error


# ################################################################################################
def main(*args)->None:
    """_summary_ : Code execution start from here.
    Arg(s):
        args: Variable Length Positional Argument
    Return(s):
        None
    """
    try:
        s = Sample("Arjun Prajapati"); s.show_data()
        ss = Sample("Jiya Chaturvedi"); ss.show_data()
        
        m = Sample("Sudhanshu Mishra"); m.show_data()
        mm = Sample("Shivani Chaturvedi"); mm.show_data()
        
        Sample.print_count()
        Sample.show_count()
    except Exception as e:
        print(e)
# #################################################################################################



if __name__ == "__main__":
    main()

