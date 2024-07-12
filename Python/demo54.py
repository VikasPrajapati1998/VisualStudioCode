import sys, random, functools


# =========================================================================
def main(*args):
    try:
        # lst
        lst = [x*3 for x in range(1, 11)]
        print("list : ", lst)
        
        m1 = list(map(lambda n: n**2, lst))
        print("map : ", m1)
        
        f1 = list(filter(lambda n: n % 6 == 0, lst))
        print("filter : ", f1)
        
        r1 = functools.reduce(lambda n, m: n + m, lst)
        print("reduce : ", r1)
    
    except Exception as e:
        print("main error : ", e)

# =========================================================================




if __name__ == "__main__":
    main()
