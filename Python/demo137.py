def parent(num):
    print("Printing from parent.")

    def first_child():
        print("Printing from first_child().")
    
    def second_child():
        print("Printing from second child().")
    
    if num == 1:
        return first_child
    else:
        return second_child


def main(*args):
    try:
        first = parent(1)
        second = parent(2)
        print()
        
        print("Function calling ....!")
        second()
        first()
    
    except AssertionError as ae:
        print("AssertionError : ", ae)
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()
