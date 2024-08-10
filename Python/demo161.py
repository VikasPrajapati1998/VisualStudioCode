def main(*args):
    try:
        """
        Fibonacci Series: Series of numbers in which each number is the sum of the two preceding numbers.
        """
        a, b = 0, 1
        size = int(input("Enter the size of number : "))
        print("Fibonacci Series : ", end=" ")
        print(a, b, end=", ", sep=", ")
        for x in range(size):
            c = a + b
            a, b = b, c
            print(c, end=", ") 
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()
    


if __name__ == "__main__":
    main()
