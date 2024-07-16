
def fabonici(n):
    lst=[]
    n = n - 2
    a = 0
    b = 1
    lst.append(a)
    lst.append(b)
    i = 0
    while i < n:
        c = a + b
        a = b
        b = c
        lst.append(c)
        i += 1
    return lst

def display(n):
    n=list(n)
    for i in n:
        print(i)
