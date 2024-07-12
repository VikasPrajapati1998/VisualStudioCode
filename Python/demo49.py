import sys, random

def fun_A():
    print("You are in function A.")

def fun_B():
    print("You are in function B.")
    
def fun_C():
    print("You are in function C.")
    
def fun_D():
    print("You are in function D.")
    
def fun_E():
    print("You are in function E.")
    
def fun_F():
    print("You are in function F.")


def main(*args):
    try:
        fun_lst = [fun_A, fun_B, fun_C, fun_D, fun_E, fun_F]
        for f in fun_lst:
            f()
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()


