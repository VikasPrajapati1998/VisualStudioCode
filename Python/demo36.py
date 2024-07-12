import operator
import random

def main(*args : tuple) -> None :
    try :
        # list comprehension ================================================================
        lst1 = [random.randint(10, 100) for n in range(21)]
        print(lst1)
        
        lst2 = [(x, x**2, x**3) for x in range(11)]
        print(lst2)
        
        lst3 = [str(x*10) for x in range(1, 21)]
        print(lst3)
        
        arr = [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]
        lst4 = [n for ele in arr for n in ele]
        print(lst4)
        
        lst5 = [*arr[0], *arr[1], *arr[2]]
        print(lst5)
        
        lst6 = [(a, b) for a in range(10, 15) for b in range(1, 5)]
        print(lst6)
        
        lst7 = [a+b for a in [1, 2, 3] for b in [4, 5, 6]]
        print(lst7)
        
        lst8 = [(i, j, k) for i in [1, 2, 3] for j in ['a', 'b', 'c'] for k in ['i', 'ii', 'iii']]
        print(lst8)
        
        # set comprehension =================================================================
        st1 = {x**2 for x in range(1, 11)}
        print(st1)
        
        st2 = {n for n in range(10, 100) if n<20 or n>80}
        print(st2)
        
        st3 = {random.randint(1, 10) for n in range(20)}
        print(st3)
        
        # dictionary comprehension ==========================================================
        dct1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
        print(dct1)
        dct2 = {k: v**2 for (k, v) in dct1.items()}
        print(dct2)
        dct3 = {k: v**2 for (k, v) in dct1.items() if v > 3}
        print(dct3)
        dct4 = {k: ('Even' if v%2 == 0 else 'Odd') for (k, v) in dct1.items()}
        print(dct4)
        print()
        
        # =========================================== Problem ================================
        print("============================= Problems ===============================")
        lst = [num for num in range(2, 51) if num%2 == 0 and num%4 == 0]
        print(lst)
        
        mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        a = [num for lst in mat for num in lst]
        print(a)
        b = [*mat[0], *mat[1], *mat[2]]
        print(b)
        
        st = {random.randint(15, 45) for num in range(10)}
        count1 = len(st)
        print(st, "len = ", count1)
        
        st = {num for num in st if num > 30}
        count2 = len(st)
        print(count1 - count2)
        print(st, "len = ", count2)
        
        # print(int(15 + 30 * random.random()))
        lst = []
        tpl = ()
        st = {}
        dct = dict()
        
        if not lst:
            print("Empty list.")
        if not tpl:
            print("Empty tuple.")
        if not st:
            print("Empty set.")
        if not dct:
            print("Empty dictionary.")
        
        
    
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

