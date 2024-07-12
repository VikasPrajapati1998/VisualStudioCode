# Write a recursive function to obtain first 15 numbers of a Fibonacci sequence.
# In a Fabonacci sequence the sum of two successive terms gives the third term.
# First few terms of the Fibonacci sequence.
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 .....

def fabonacci(previous=1, current=1, terms=1):
    try:
        if terms >= 1:
            next = previous + current
            print(f"{next:<20}", end=" ")
            previous, current = current, next
            terms -= 1
            if terms%5 == 0:
                print()
            fabonacci(previous, current, terms)
    
    except Exception as e:
        print("fabonacci error : ", e)


def main(*args):
    try:
        fabonacci(1, 1, 50)
    
    except Exception as e:
        print("main error : ", e)




if __name__ == "__main__":
    main()


