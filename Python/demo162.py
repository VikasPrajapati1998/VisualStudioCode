def main(*args):
    try:
        lst = [x for x in range(1, 10)]
        tpl = tuple([x for x in range(1, 10)])
        print(lst)
        print(tpl)
        
        lst[4] = 99
        print(lst)
        
        tpl[4] = 99
        print(tpl)
        
    except Exception as e:
        print("main error : ", e)
        print(e.__annotations__)
    
    finally:
        print()


if __name__ == "__main__":
    main()


