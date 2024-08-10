def main(*args):
    """
    Largest Among n digit.
    """
    try:
        arr = []  # empty list
        num = int(input("Enter size : "))
        for n in range(num):
            numbers = int(input("Enter number : "))
            arr.append(numbers)
        print("Maximum element in the list is : ", max(arr))
        print("Minimum element in the list is : ", min(arr))
        
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()


if __name__ == "__main__":
    main()



        