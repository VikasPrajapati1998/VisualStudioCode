# ==================== Comprehension ========================
import random


# list Comprehension
lst1 = [random.randint(10, 100) for x in range(10)]
print(lst1)

lst2 = [(x, x**2, x**3) for x in range(1, 10)]
print(lst2)

lst3 = [float(x) for x in range(1, 10)]
print(lst3)

lst4 = [k for k in range(10, 50) if k%2 == 0]
print(lst4)

lst5 = [k for k in lst4 if k>20 and k<40]
print(lst5)

# flatten a list of lists
arr = [[k*2 for k in range(1, 10)],
       [k*5 for k in range(1, 10)],
       [k*7 for k in range(1, 10)]]
print(arr)

arr_b = [n for ele in arr for n in ele]
print(arr_b)
arr_c = [*arr[0], *arr[1], *arr[2]]
print(arr_c)

# nested loop
lst1 = [k for k in range(1, 6)]
lst2 = [k*2 for k in range(1, 6)]
print(lst1, lst2)
lst3 = [a+b for a in lst1 for b in lst2]
print(lst3)
lst4 = [(a, b) for a in lst1 for b in lst2]
print(lst4)


