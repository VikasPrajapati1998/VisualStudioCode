def printMyName(name):
    print(f"My name is {name}.")


def foo(fun, name:str):
    assert isinstance(name, str), "Name should be string."
    return fun(name)


def main(*args):
    try:
        foo(printMyName, 123)
    
    except AssertionError as ae:
        print("AssertionError : ", ae)
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()
