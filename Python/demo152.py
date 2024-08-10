def factorial(num):
    assert num >= 0, "Number is negative."
    
    fact = 1
    for x in range(num+1):
        if x == 0:
            fact = 1
        else:
            fact *= x
        yield fact



def main(*args):
    """
    Factorial of a number is the product of the number and all numbers below it.
    """
    try:
        import sys
        
        num = int(input("Enter a number : "))
        fact_gen = factorial(num)
        print(list(fact_gen))
        fact = 1
        for f in fact_gen:
            fact = f
        print(fact)
        print(sys.getsizeof(fact))
        
            
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()




if __name__ == "__main__":
    main()
