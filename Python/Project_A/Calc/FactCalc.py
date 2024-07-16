def factorial(a):
    fact=1
    for i in range(a+1):
        if i==0:
            pass
        elif i==1:
            pass
        elif i>1:
            fact*=i
        else:
            fact="Got some error."
    return fact

def show(n):
    print(n)
