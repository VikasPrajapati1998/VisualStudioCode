from array import *
arr = array('i', [])
n = int(input("Enter Length of array = "))
for i in range(n):
    x = int(input("Enter Value "+str(i+1)+" = "))
    arr.append(x)
print(arr)

vals = arr
print(vals)
print("buffer_info = ", vals.buffer_info())
print("typecode = ", vals.typecode)
vals.reverse()
print("reverse = ", vals)
arr = array('i', [])
print("empty array = ", arr)
print("empty array = ", vals)

