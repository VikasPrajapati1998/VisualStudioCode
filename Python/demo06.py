# Write a program to read 10 sets of p, r, n & q and calculate the corresponding as.
# a = p (1+r/q)**nq
p = float(input("Enter Principle Ammount : "))
r = float(input("Enter Rate : "))
n = int(input("Number of Year : "))
q = int(input("Enter Years : "))

a = p*(1 +r/q)**(n*q)
print("Amount : {:.2f}".format(a))
