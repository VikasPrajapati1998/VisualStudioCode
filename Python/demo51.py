# import sys, random

def main(*args):
    try:
        fun = [lambda x: x**2, 
               lambda x: x**3, 
               lambda x: x**4,
               lambda x: x**5]
        
        lst = [4, 8, 12, 16]
        
        lst_result = []
        
        for var, f in zip(lst, fun):
            lst_result.append((var, f(var)))
        
        print(lst_result)
        
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()

