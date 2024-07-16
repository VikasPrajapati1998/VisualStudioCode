def fun(n):
    return lambda a: a*n

s = int(input("Enter Power = "))
t = fun(s)
w = int(input("Enter Base = "))
print(t(w))

v = lambda p: s**w
print(v(1))

h = lambda l: "Hello user"
print(h(1))
