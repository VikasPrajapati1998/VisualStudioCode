# Synchronization
'''
Lock : Mutex, Atomicity
RLock
Semaphore
'''
import threading
import time

sum = 0
rlck = threading.RLock()

def fun1(num: int):
    rlck.acquire()
    global sum
    for x in range(1, num):
        sum += x
        print(f"fun1: {sum} ")
        time.sleep(0.5)
    rlck.release()
    print()


def fun2(num: int):
    rlck.acquire()
    global sum
    for x in range(1, num):
        sum += x
        print(f"fun2: {sum} ")
        time.sleep(0.5)
    rlck.release()
    print()


def fun3(num: int):
    rlck.acquire()
    global sum
    for x in range(1, num):
        sum += x
        print(f"fun3: {sum} ")
        time.sleep(0.5)
    rlck.release()
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
    
    print(sum)


if __name__ == "__main__":
    main()
