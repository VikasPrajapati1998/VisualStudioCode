# Set Comprehension
import random

set1 = {x**2 for x in range(1, 10)}
print(set1)

set2 = {k for k in set1 if k<20 or k>50}
print(set2)

# Dictionary Comprehension
dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
d1 = {k: v**3 for (k, v) in dct.items()}
print(d1)

d2 = {k: v**3 for (k, v) in dct.items() if v>3}
print(d2)

d3 = {k: ('Even' if v%2==0 else 'Odd') for (k, v) in dct.items()}
print(d3)

d4 = [k for k in range(2, 51) if k%2==0 and k%3==0]
print(d4)


