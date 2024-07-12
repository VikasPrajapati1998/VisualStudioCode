import sys, random, operator


def num_sum(limit):
    if limit <= 0:
        return 0
    else:
        sum = limit + num_sum(limit - 1)
    return sum


def main(*args):
    try:
        num = int(input("Enter a number : "))
        sum = num_sum(num)
        print("Sum = ", sum)
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()


