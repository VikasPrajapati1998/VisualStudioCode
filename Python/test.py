lst1 = [x for x in range(1, 10)]
lst2 = [x**2 for x in range(1, 10)]

lst1 = sorted(list(set(lst1 + lst2)))
lst = lst1 + lst2

print(lst1)
print(lst)

