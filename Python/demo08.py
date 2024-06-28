random_lst = [7, 3, 9, 4, 1, 2, 5, 8, 6]
lst = [x**2 for x in random_lst]
print(lst, id(lst))
print()

print("------------------------------------- len, sum, max, min, any, all -----------------------------")
print(len(lst), sum(lst))
print(max(lst), min(lst))
print(any(lst), all(lst))
print()

print("---------------------------------------------- copy, del ----------------------------------------")
lst_copy = lst.copy()
print(lst_copy)
del(lst_copy)
print(lst)
print()

print("---------------------------------------- id, sorted, rerversed ----------------------------------")
list_copy = lst.copy()
print(list_copy, id(list_copy))
print(sorted(lst))
print(sorted(list_copy, reverse=True))
print(lst)
print(list(reversed(lst)))
print()

print("------------------------------- append, removed, pop, insert, count, index ----------------------")
lst.append(12); print(lst)
lst.remove(1); print(lst)
lst.pop(); print(lst)
lst.pop(4); print(lst)
lst.insert(3, 36); print(lst)
print(lst.count(36))
print(lst.index(25))
print()

print("--------------------------------------------- reverse, sort -------------------------------------")
lst.reverse()
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
print()


