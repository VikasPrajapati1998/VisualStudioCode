# Without Lock

import time
import threading

rlck = threading.RLock()

def factorial(num):
    # rlck.acquire()
    fact = 0
    if num != 0:
        t = threading.current_thread()
        fact = num * factorial(num - 1)
        print(t.name, ":", num, "! = ", fact)
    else:
        fact = 1
    # rlck.release()
    return fact


def main(*args):
    try:
        t1 = threading.Thread(target=factorial, args=(6,))
        t2 = threading.Thread(target=factorial, args=(9,))
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()


if __name__ == "__main__":
    main()

