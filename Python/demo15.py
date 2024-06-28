# Concatenate ============================================
lst = [12, 15, 13, 23, 22, 16, 17]
lst = lst + [33, 44, 55]
print(lst)

print("--------------------------------------------------")

tpl = (12, 15, 12, 23, 22, 16, 17)
tpl = tpl + (33, 44, 55)
print(tpl)

print()
# Merging ================================================
lst_s = [10, 20, 30]
lst_t = [100, 200, 300]
lst_z = lst_s + lst_t
print(lst_z)

print("--------------------------------------------------")

tpl_s = (10, 20, 30)
tpl_t = (100, 200, 300)
tpl_z = tpl_s + tpl_t
print(tpl_z)

print()
# Conversion =============================================
lst_l = list("Africa")
print(lst_l)

print("--------------------------------------------------")

tpl_l = tuple("Africa")
print(tpl_l)

print()
# Aliasing ===============================================
lst1 = [x for x in range(10, 60, 10)]
lst2 = lst1
print(lst1)
print(lst2)
lst1[0] = 100
print(lst1[0], lst2[0])

print("--------------------------------------------------")

tpl1 = tuple(x for x in range(10, 60, 10))
tpl2 = tpl1
print(tpl1)
print(tpl2)

print()
# Cloning ================================================
lst1 = [x for x in range(10, 60, 10)]
lst2 = []
lst2 = lst2 + lst1
print(lst1, id(lst1))
print(lst2, id(lst2))

print("--------------------------------------------------")

tpl1 = tuple(x for x in range(10, 60, 10))
tpl2 = tuple()
tpl2 = tpl2 + tpl1
print(tpl1, id(tpl1))
print(tpl2, id(tpl2))

print("--------------------------------------------------")

print(lst1 is lst2)
print(tpl1 is tpl2)

print()
# Searching ===============================================
lst = list('aeiou')
print('a' in lst)
print('z' not in lst)
print('x' in lst)
print('e' not in lst)

print("--------------------------------------------------")

tpl = tuple('aeiou')
print('a' in tpl)
print('z' not in tpl)
print('x' in tpl)
print('e' not in tpl)

print()
# Identity ================================================
lst1 = [x for x in range(10, 60, 10)]
lst2 = [x for x in range(10, 60, 10)]
lst3 = lst1
print(id(lst1), id(lst2), id(lst3))
print(lst1 is lst2) # False
print(lst1 is lst3) # True
print(lst1 is not lst2) # True

print("--------------------------------------------------")

tpl1 = tuple(x for x in range(10, 60, 10))
tpl2 = tuple(x for x in range(10, 60, 10))
tpl3 = tpl1
print(id(tpl1), id(tpl2), id(tpl3))
print(tpl1 is tpl2) # False
print(tpl1 is tpl3) # True
print(tpl1 is not tpl2) # True

print()
# Comparison ===============================================
lst_a = [1, 2, 3, 4]
lst_b = [1, 2, 5]
print(lst_a < lst_b)

print("--------------------------------------------------")

tpl_a = (1, 2, 3, 4)
tpl_b = (1, 2, 5)
print(tpl_a < tpl_b)

print()
# Emptiness ================================================
lst = []
tpl = ()

if not lst:
    print("Empty list.")

if not tpl:
    print("Empty tuple.")

