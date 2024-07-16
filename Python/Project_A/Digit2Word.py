"""
Write a Python code to read an integer in a file e.g 123 and convert it to words
e.g One hundred and twenty three and write the result back to the same file such that
your file will have "123 One hundred and twenty three " in it
"""
import os
x = ""
def get_num(a):
    global x
    num = {
        '0': "Zero",
        '1': "One",
        '2': "Two",
        '3': "Three",
        '4': "Four",
        '5': "Five",
        '6': "Six",
        '7': "Seven",
        '8': "Eight",
        '9': "Nine",
    }
    for i, j in num.items():
        if i==a:
            x = j
            return x


file = open("number.txt", "r")
p = file.read()
print(p)
val = ""
n1 = get_num(p[0])
v1 = n1 + " " + "Thousand"

n2 = get_num(p[1])
v2 = n2 + " " + "Hundred"

m = int(p[2:4])
if m == 11 or m == 12:
    if m==11:
        v3 = "Eleven"
    else:
        v3 = "Twelve"
elif m>12 and m<20:
    n4 = get_num(p[3])
    v4 = n4
    v3 = v4+"teen"
    v4 = ''
else:
    n3 = get_num(p[2])
    v3 = n3 + "ty"
    n4 = get_num(p[3])
    v4 = n4

val = v1+" "+v2+" "+v3+" "+ v4
print(val)

file.close()

f = open("number.txt", "a")
f.write(" "+val)
f.close()

f = open("number.txt", "a")
os.remove(f)
f.close()



