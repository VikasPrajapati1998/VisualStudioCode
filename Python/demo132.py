def main(*args):
    number = int(input("Enter a number : "))
    if number > 10:
        raise Exception(f"The number is greater than 10.")
    print(number)

def foo(*args):
    number = int(input("Enter a number : "))
    assert (number < 10)
    print(number)

def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux system.")
    print("Doing Linux things.")

def linux():
    try:
        linux_interaction()
    except RuntimeError as error :
        print(error)
        print()
        print(error.__annotations__())



if __name__ == "__main__":
    linux()


