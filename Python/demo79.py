# Iterators

def main(*args):
    try:
        for ch in "Good Afternoon":
            print(ch, end=', ')
        print()
        
        for num in [10, 20, 30, 40, 50]:
            print(num, end=', ')
        print()
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()

