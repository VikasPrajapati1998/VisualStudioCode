def main(*args):
    try:
        """ Swapping in python. Without using third variable. """
        x = int(input("Enter a number : "))
        y = int(input("Enter a number : "))
        print(f"Before Swapping : x={x}, y={y}")
        x, y = y, x
        print(f"After Swapping : x={x}, y={y}")
    
    except Exception as e:
        print("main error : ", e)




if __name__ == "__main__":
    main()

