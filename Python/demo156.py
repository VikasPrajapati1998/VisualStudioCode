def Prime(num: int) -> None:
    try:
        # num = int(input("Enter a number: "))
        
        if num <= 1:
            # print(f"{num} : Not Prime")
            return
        else:
            for x in range(2, num//2 + 1):
                if num % x == 0:
                    # print(f"{num} : Not Prime")
                    break
            else:
                print(num, end=", ")
        
    
    except Exception as e:
        print("prime error : ", e)



def main(*args):
    try:
        n = int(input("Enter a number: "))
        for x in range(n):
            Prime(x)
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()
    


if __name__ == "__main__":
    main()

