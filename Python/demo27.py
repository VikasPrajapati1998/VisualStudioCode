def print_it(x, y, *args, a, b, **kwargs) :
    try:
        print("x = ", x, "y = ", y)
        
        print("Args = ")
        for k in args:
            print(k, end=", ")
        
        print("a = ", a, "b = ", b)
        
        print("Kwargs = ")
        for k, v in kwargs.items():
            print(k, v, end=", ")
    
    except Exception as e:
        print("print_it() Error : ", e)
    
    finally:
        print()
        
        

def main():
    try:
        # Functional Programming
        print_it(10, 20, 100, 200, a=5, b=7, p=2, l=4, m=6, n=8)
    
    except Exception as e:
        print(e)
        
    finally:
        print("Program Finish")
        print()
        

if __name__ == "__main__":
    main()
