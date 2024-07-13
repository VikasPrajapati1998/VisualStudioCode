from messages.funny.modf1 import *
from messages.funny.modf2 import *
from messages.funny.modf3 import *

from messages.curt.modc1 import *
from messages.curt.modc2 import *
from messages.curt.modc3 import *


def main(*args):
    try:
        alpha_f1()
        beta_c2()
        gama_f3()
        
        
    except Exception as e:
        print("main error : ", e)
    

if __name__ == "__main__":
    main()

