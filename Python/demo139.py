def decorator(func):
    def wrapper():
        print("Something is happending before the function call.")
        func()
        print("Something is happending after the function call.")
    return wrapper


@decorator
def foo():
    print("Printing from the foo..")


def main(*args):
    try:
        foo()
    
    except AssertionError as ae:
        print("AssertionError : ", ae)
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()
