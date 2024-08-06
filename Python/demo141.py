import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(name):
        print("Something is happending before the function call.")
        func(name)
        print("Something is happending after the function call.")
    return wrapper


@decorator
def foo(name):
    print("Printing from the foo..")
    assert isinstance(name, str), "Name should be only string."
    print(f"My name is {name}.")

# foo = decorator(foo)

def main(*args):
    try:
        foo("Arjun")
        foo(234)
    
    except AssertionError as ae:
        print("AssertionError : ", ae)
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()


if __name__ == "__main__":
    main()
