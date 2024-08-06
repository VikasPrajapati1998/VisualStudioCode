def foo():
    print("Hello Programmer.")


def decorator(fun):
    def wrapper():
        print("Welcome Programmer.")
        fun()
        print("Bye Bye Coder")
    return wrapper

foo = decorator(foo)


def main(*args):
    try:
        foo()

        print()
        
    except Exception as e:
        print("main error : ", e)
    
    else:
        print("No error found.")
    
    finally:
        print("Program end.")
        print()



if __name__ == "__main__":
    main()

