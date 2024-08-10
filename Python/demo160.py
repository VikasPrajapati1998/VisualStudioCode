def main(*args):
    try:
        x = int(input("Enter a number : "))
        y = int(input("Enter a number : "))
        print(f"Before Swapping : x={x}, y={y}")
        x = x + y
        y = x - y
        x = x - y
        print(f"After Swapping : x={x}, y={y}")
    
    except Exception as e:
        print("main error : ", e)




if __name__ == "__main__":
    main()

