import operator, random

# functional programming

def print_it(i, j, *args, x=0, y=0, **kwargs):
    # positional arguments
    # variable-length positional arguments
    # keyword arguments
    # variable-length keyword arguments
    try:
        print("Positional Arguments : ", i, j)
        
        print("Variable Length Positional Arguments : ", end=" ")
        for k in args:
            print(k, end=", ")
        print()
        
        print("Keywords Arguments : ", x, y)
        
        print("Variable Length Keywords Arguments : ")
        for k, v in kwargs.items():
            print(f'{k:>38} : {v}')
        print()        
        
    
    except Exception as e:
        print("Print_it Error : ", e)
    

def main(*args) -> None:
    try:
        print_it(1, 2)
        print_it(1, 2, 3)
        print_it(2, 4, 6, 8, 10)
        
        print_it(2, 4, 6, 8, 10, 12, x=14)
        print_it(3, 6, 9, 12, 15, 18, x=21, y=24)
        
        print_it(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, x=22, y=24, l=10, m=20, n=30)
        print_it(i=2, j=4, args=(3, 6, 9), x=9, y=18, kwargs={'p':1, 'q':2, 'r':3})  # error 
        print_it(2, 4, 3, 6, 9, x=9, y=18, p=1, q=2, r=3) 
        
    
    except Exception as e:
        print("Main Error : ", e)


if __name__ == "__main__":
    main()

