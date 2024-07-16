f = open("trialfile.txt", "w")
f.write("Adding a new line.")
f.close()

f = open("trialfile.txt", "r")
print(f.read())
f.close()
