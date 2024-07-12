import sys, random, functools


def map_fun(n):
    return n**2

def filter_fun(n):
    return (n % 5 == 0) if True else False

def reduce_fun(x, y):
    return x + y


# ===================================================================
def main(*args):
    try:
        # list
        lst = [x for x in range(5, 101, 5)]
        print("Actual List : ", lst)
        
        # map
        m1 = list(map(map_fun, lst))
        print("Map List : ", m1)
        
        # filter
        f1 = list(filter(filter_fun, lst))
        print("Filter List : ", f1)
        
        # reduce
        r1 = functools.reduce(reduce_fun, lst)
        print("Reduce Result : ", r1)
        
        
    except Exception as e:
        print("main error : ", e)
# ===================================================================


if __name__ == "__main__":
    main()
