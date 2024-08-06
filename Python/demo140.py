def decorator(func):
    def wrapper(name):
        print("Something is happending before the function call.")
        func(name)
        print("Something is happending after the function call.")
    return wrapper


@decorator
def foo(name):
    print("Printing from the foo..")
    print(f"My name is {name}.")

# foo = decorator(foo)

def main(*args):
    try:
        foo("Arjun")
    
    except AssertionError as ae:
        print("AssertionError : ", ae)
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()
