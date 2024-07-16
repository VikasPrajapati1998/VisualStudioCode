print("Method = 1:")
f = open("testfile.txt", 'r')
data = f.read()
print(data)
f.close()
print()

print("Method = 2:")
f = open("testfile.txt", 'r')
data = f.readline()
print(data)
f.close()
print()

print("Method = 3:")
with open("testfile.txt", 'r') as f:
    data = f.read()
    print(data)
print()

print("Method = 3:")
with open("testfile.txt", 'r') as f:
    print('First time:- data1')
    data1 = f.read()
    print(data1)
    print('Second time:- data2')
    data2 = f.read()
    print(data2)
print()

print("Method = 4:")
with open("testfile.txt", 'r') as f:
    line = f.readline()
    print(line)
    line = f.readline(20)
    print(line)
print()

print("Method = 4:")
with open("testfile.txt", 'r') as f:
    line = f.readline()
    print(line)
    # Operation on a single line on line-02
    line = f.readline(15)
    print(line)
    line = f.readline(25)
    print(line)
    line = f.readline()
    print(line)
    # Here line-02 finished.
print()

print("Method = 5:")
with open('testfile.txt', 'r') as f:
    line = f.readline(20)
    print(line)
    data = f.seek(0, 1) # Beginning to current position of file
    print(data)
    data = f.seek(0, 2) # Beginning to end of the file
    print(data)
    data = f.seek(25, 0) # 25th position to beginning
    print(data)
print()

with open('testfile.txt', 'r') as f:
    data = f.seek(0) # 25th position to beginning, negative say in right direction end means beginning
    print(data)



