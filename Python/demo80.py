# iterator
def main(*args):
    try:
        lst = [x*10 for x in range(1, 10)]
        print(lst)
        
        it = lst.__iter__()
        print(it.__next__(), end=", ")
        print(it.__next__(), end=", ")
        print(it.__next__(), end=", ")
        print(it.__next__(), end=", ")
        print(it.__next__(), end=", ")
        print(it.__next__())
        
        it = iter(lst)
        print(next(it), end=", ")
        print(next(it), end=", ")
        print(next(it), end=", ")
        print(next(it), end=", ")
        print(next(it), end=", ")
        print(next(it))
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()

