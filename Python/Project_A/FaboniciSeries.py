n = int(input("Enter Limit of Series = "))
n = n - 2
a = 0
b = 1
print(a)
print(b)
i = 0
while i < n:
    c = a + b
    a = b
    b = c
    print(c)
    i += 1

s = str(c)
j = 0
for i in s:
    j += 1
print("Length of last digit = ", j)
