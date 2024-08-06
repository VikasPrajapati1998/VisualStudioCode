'''
# In short: Use .__repr__() for Programmers vs .__str__() for Users.
# repr() is a built-in function and str() is a class.
'''


import datetime

def main(*args):
    try:
        # When should we use .__repr__() vs .__str__() in python.
        today = datetime.datetime.now()
        print("repr() & str() functions")
        print(repr(today))
        print(str(today))
        print()
        
        print(".__repr__() & .__str__() methods")
        print(today.__repr__())
        print(today.__str__())
        print()
        
        print("format & !r & !s")
        print(format(today))
        print("{}".format(today))
        print("{!r}".format(today))
        print("{!s}".format(today))
        print()
        
        print("f'', f+!r, f+!s")
        print(f"{today}")
        print(f"{today!r}")
        print(f"{today!s}")
        print(f"{today = }")
        print(f"{today = !s}")
        print(f"{today = !r}")
        
        # Should You Define .__repr__() and .__str__() in a Custom Class
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()

