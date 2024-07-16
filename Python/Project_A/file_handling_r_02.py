f = open("testfile.txt", "r")

print("First_ReadLine-", f.readline())
print("Second_ReadLine-", f.readline(10))
print("Third_ReadLine-", f.readline())
for i in f:
    print("Loop - ", i)
f.close()
