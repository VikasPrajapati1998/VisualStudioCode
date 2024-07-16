f = open("demofile.txt", "a")
f.write("Adding a new line.\n")
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()
