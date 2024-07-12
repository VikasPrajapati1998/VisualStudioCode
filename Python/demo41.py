import operator, random


def factorize(n, i):
    try:
        if i <= n:
            if n%i == 0:
                print(i, end=", ")
                n = n // i
            else:
                i += 1
        factorize(n, i)
    
    except Exception as e:
        print("Factorize : ", e)



def main(*args)-> None: 
    try:
        num = int(input("Enter a number : "))
        print("Prime factors are : ")
        factorize(num, 2)

    except Exception as e:
        print("Main Error : ", e)




if __name__ == "__main__":
    main()

