'''
Scope:
    1. Local Scope: Inside Function
    2. Global Scope: Throughout the code execution since their inception.
    3. Module Level Scope: Global object of current module accessible in the program.
    4. Outermost Scope: All the build-in names callable in the program.
'''

import sys

# Namespace
for path in sys.path:
    print(path)
print()

b = 65
c = 7
def foo():
    print(b, c)
    
def main(*args):
    foo()
    a = 45
    b = 76
    global c
    c = 90
    print(a, b, c)
    foo()
    print()
    
    print(locals()); print()
    print(globals()); print()
    print(vars)


if __name__ == "__main__":
    main()
    
    