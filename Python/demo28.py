def main():
    try:
        # map, filter, reduce
        lst = [x for x in range(1, 21)]
        print(lst)
        # map
        lst1 = map(lambda x : x*x, lst)
        print(lst1)
    
    except Exception as e:
        print(e)
    
    finally:
        print()
        

if __name__ == "__main__":
    main()
