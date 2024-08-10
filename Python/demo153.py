def main(*args):
    """
    Prime number is a number that is division only by 1 and by itself.
    """
    try:
        count = 0
        num = int(input("Enter a number: "))
        for x in range(1, num+1):
            if num % x == 0:
                count += 1
        
        if count == 2:
            print("Prime.")
        else:
            print("Not Prime.")
                
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()




if __name__ == "__main__":
    main()

