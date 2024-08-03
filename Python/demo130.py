# Should You Define .__repr__() and .__str__() in a Custom Class

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(title={self.title!r}, author={self.author!r})"
    
    def __str__(self):
        return f'"{self.title!s}", "{self.author!s}"'


def main(*args):
    try:
        odyssey = Book("The Odyssey", "Homer")
        print(repr(odyssey))
        print(str(odyssey))
        print()
        
        sherlock = Book("Sherlock", "Holmes")
        print(repr(sherlock))
        print(str(sherlock))
        print()
        
        chetan = Book("Half Girlfriend", "Chetan Bhagat")
        print(repr(chetan))
        print(str(chetan))
        print()
        
        print(odyssey)
        print(sherlock)
        print(chetan)
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()

