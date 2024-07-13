a, b, c = 10, 20, 30

print(globals()); print()

globals()['a'] = 40
globals()['b'] = 50
globals()['c'] = 60

print(globals()); print()

print(__name__)
print(__file__)
print(__cached__)
print(__spec__)
