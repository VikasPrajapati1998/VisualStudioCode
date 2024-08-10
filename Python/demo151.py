def main(*args):
    """
    Factorial of a number is the product of the number and all numbers below it.
    """
    try:
        import sys
        
        fact = 1
        num = int(input("Enter a number : "))
        assert num >= 0, "Number is negative."
        for x in range(num+1):
            if x == 0:
                fact = 1
            else:
                fact *= x
        print(fact)
        print(sys.getsizeof(fact))
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()





if __name__ == "__main__":
    main()
