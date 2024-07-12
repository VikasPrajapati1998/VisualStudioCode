import random, operator
import sys

def dec2bin(num):
    try:
        
        if num >= 1:
            binary = ''
            rem = num % 2
            num = num // 2
            dec2bin(num)
            print(rem, end='')
            
    except Exception as e:
        print("dec2bin error : ", e)


def main(*args):
    try:
        sys.setrecursionlimit(10**6)
        num = int(input("Enter a number : "))
        print("Binary = ", end='')
        dec2bin(num)
        print(end="\n\n")
    
    except Exception as e:
        print("main Error : ", e)



if __name__ == "__main__":
    main()

