# Synchronization
'''
Lock : Mutex, Atomicity
RLock
Semaphore
'''
import threading
import time

sum = 0
mul = 1
lck = threading.Lock()

def fun1(num: int):
    lck.acquire()
    global sum
    global mul
    for x in range(1, num):
        sum += x
        mul *= x
        print(f"fun1: {sum}, {mul} ")
        time.sleep(0.5)
    lck.release()
    print()


def fun2(num: int):
    lck.acquire()
    global sum
    global mul
    for x in range(1, num):
        sum += x
        mul *= x
        print(f"fun2: {sum}, {mul} ")
        time.sleep(0.5)
    lck.release()
    print()


def fun3(num: int):
    lck.acquire()
    global sum
    global mul
    for x in range(1, num):
        sum += x
        mul *= x
        print(f"fun3: {sum}, {mul} ")
        time.sleep(0.5)
    lck.release()
    print()


def main(*args):
    t1 = threading.Thread(target=fun1, args=(10,))
    t2 = threading.Thread(target=fun2, args=(10,))
    t3 = threading.Thread(target=fun3, args=(10,))
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    print(f"sum = {sum}, mul = {mul}")


if __name__ == "__main__":
    main()
