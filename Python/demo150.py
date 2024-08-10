def main(*args):
    """
    Number is even or odd.
    """
    try:
        n = int(input("Enter a number : "))
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")
    
    except Exception as e:
        print("main error : ", e)





if __name__ == "__main__":
    main()


