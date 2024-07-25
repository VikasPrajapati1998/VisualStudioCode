# zip() Function

def main(*args):
    try:
        alpha = [chr(x) for x in range(65, 75)]
        num = [x for x in range(65, 75)]
        
        it = zip(alpha, num)
        print(it)
        
        lst = list(it)
        print(lst)
        lst1 = list(it)
        print(lst1)
        
        it = zip(alpha, num)
        tpl = tuple(it)
        print(tpl)
        tpl1 = tuple(it)
        print(tpl1)
        
        it = zip(alpha, num)
        st = set(it)
        print(st)
        st1 = set(it)
        print(st1)
        
        it = zip(alpha, num)
        fst = frozenset(it)
        print(fst)
        fst1 = frozenset(it)
        print(fst1)
        
        print()
        
        it = zip(alpha, num)
        lst = list(it)
        w, n = zip(*lst)
        print(w)
        print(n)
        print()
        
        it = zip(alpha, num)
        lst = list(it)
        print(lst)
        print(list(zip(*lst)))
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()

