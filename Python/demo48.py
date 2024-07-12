# Functional Programming : function, lambda, map, filter, reduce
import sys

def fun():
    print("Welcome Programmer.")

def sum(x:int, y:int):
    print(x+y)

# ==============================================================
def main(*args):
    try:
        f = fun
        f()
        
        g = sum
        g(5, 7)
    
    except Exception as e:
        print("main error : ", e)
# ==============================================================



if __name__ == "__main__":
    main()
