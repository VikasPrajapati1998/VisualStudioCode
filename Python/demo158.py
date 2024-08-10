def main(*args):
    try:
        """ Swapping in python. Using third variable."""
        x = int(input("Enter a number : "))
        y = int(input("Enter a number : "))
        print(f"Before Swapping : x={x}, y={y}")
        temp = x
        x = y
        y = temp
        print(f"After Swapping : x={x}, y={y}")
    
    except Exception as e:
        print("main error : ", e)




if __name__ == "__main__":
    main()

