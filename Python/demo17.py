import operator
 # each embedded tuple/list contains name, age, salary
 
lst = [("Shailesh", 24, 3455.50), ("Priyanka", 25, 4555.50)]
tpl = (["Shailesh", 24, 3455.50], ["Priyanka", 25, 4555.50])
print(sorted(lst))
print(sorted(tpl))
print()
print(sorted(lst, key=operator.itemgetter(2)))  # sorted by salary, 2 is index number
print(sorted(tpl, key=operator.itemgetter(2)))
print()


