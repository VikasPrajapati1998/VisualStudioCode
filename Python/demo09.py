lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6, 8, 10]
lst = lst1 + lst2
print(lst)

lst = [3, 6, lst1, 12, 15, 18]
print(lst)
lst = [6, 5, 4, 3*lst2, 2, 3, 4]
print(lst)

lst = [1, 2, 3, *lst1, 4, 5]
print(lst)


