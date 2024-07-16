f = open("testfile.txt", "r")
print(f.read())
f.close()
print()
f = open("testfile.txt", "r")
for x in f:
    print(x)
f.close()

