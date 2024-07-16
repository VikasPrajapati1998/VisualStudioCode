def nondivisible(x):
    for n in range(2,x):
        if x%n == 0:
            return False
        else:
            return True

f = filter(nondivisible, range(50))
print(list(f))

def squr(x):
    return x*x

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
m = map(squr, lst1)
print(list(m))
