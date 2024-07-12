import sys, random

def squire(x):
    return (x**2)

def cube(x):
    return (x**3)

def absolute(x):
    if x<0:
        return (x*(-1)) 
    else:
        return (x)

def power4(x):
    return (x**4)

def power5(x):
    return (x**5)


def main(*args):
    try:
        fun = [squire, cube, absolute, power4, power4, power5]
        lst = [2, 3, 4, 5, 6, 7]
        lst_result = []
        
        for var, f in zip(lst, fun):
            lst_result.append((var, f(var)))
        
        print(lst_result)
            
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()

