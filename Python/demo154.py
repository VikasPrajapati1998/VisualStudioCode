def main(*args):
    try:
        num = int(input("Enter a number: "))
        
        if num <= 1:
            print(f"{num} : Not Prime")
        else:
            for x in range(2, num//2 + 1):
                if num % x == 0:
                    print(f"{num} : Not Prime")
                    break
            else:
                print(f"{num} : Prime")
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()
    


if __name__ == "__main__":
    main()

