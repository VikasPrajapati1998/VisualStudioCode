# Problem 14.3 : Paper of size A0 has dimensions 1189mm x 841mm. Each subsequent size A(n) is defined as A(n-1) cut in half,
# parallel to its shorter sides.
# Write a program to calculate and print paper sizes A0, A1, A2 ......... A8 using recursion.

import random, operator

# ===================================================================================
def papersizes(i, n, length, breath):
    try:
        if n != 0:
            print(f'A{i}: L = {int(length)} B = {int(breath)}')
            new_breath = length / 2
            new_length = breath
            n -= 1
            i += 1
            papersizes(i, n, new_length, new_breath)
            
    
    except Exception as e:
        print("papersized Error : ", e)

# ===================================================================================


# ###################################################################################
def main(*args) :
    try:
        i, n = 0, 7
        length, breath = 1189, 841
        papersizes(i, n, length, breath)
    
    except Exception as e:
        print("main Error : ", e)
    
    finally:
        print("Function main() ends.")

# ###################################################################################



if __name__ == "__main__":
    main()

