def Prime(a):
    i = 2
    count = 0
    while i < a:
        if a % i == 0:
            count += 1
        i += 1
    if count == 0:
        print("Prime Number")
    else:
        print("Not Prime Number")


a = int(input("Enter a number = "))
if a>0:
    Prime(a)
else:
    print("Enter a positive non zero number")
