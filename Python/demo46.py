import sys, random, operator


# --------------------------------------------------------------------
# Tail Recursion:
def tail_recursion(num, sum=0):
    if num == 0:
        return sum
    else:
        return tail_recursion(num - 1, sum + num)
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# Head Recursion:
def head_recursion(num):
    if num == 0:
        return 0
    else:
        return num + head_recursion(num - 1)
# --------------------------------------------------------------------



# ====================================================================
# main function
def main(*args):
    try:
        num = int(input("Entr a number : "))
        
        head_sum = head_recursion(num)
        print("head_sum = ", head_sum)
        
        tail_sum = tail_recursion(num)
        print("tail_sum = ", tail_sum)
    
    except Exception as e:
        print("main error : ", e)
# ====================================================================


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()

