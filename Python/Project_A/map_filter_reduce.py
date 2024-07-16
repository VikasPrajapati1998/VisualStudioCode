from functools import reduce

def main():
    lst = []
    n = int(input("How many numbers you want to enter : "))
    """ taking input of list """
    for i in range(n):
        a = int(input("Enter "+str(i+1)+" value : "))
        lst.append(a)

    # printing list
    print("List : ", lst)

    # using map function to make the square of each element
    print("Square of each element : ", list(map(lambda l: l*l, lst)))

    # using filter function to filter out the even and odd elements of list
    print("Even values of list : ", list(filter(lambda l: l%2==0, lst)))
    print("Odd values of list : ", list(filter(lambda l: l%2!=0, lst)))

    # using reduce function
    print("Sum of hole list : ", reduce(lambda l, m: l+m, lst))
    print("Multiplication of hole list : ", reduce(lambda l, m: l*m, lst))

if __name__ == "__main__":
    main()
