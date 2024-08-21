import time
import threading

rlck = threading.RLock()

def squares(nos):
    rlck.acquire()
    print("Calculating Squares : ")
    for n in nos:
        time.sleep(0.5)
        print('n = ', n, 'square = ', n*n)
    rlck.release()
    print()


def cubes(nos):
    rlck.acquire()
    print("Calculating Cubes : ")
    for n in nos:
        time.sleep(0.5)
        print('n = ', n, 'cube = ', n*n*n)
    rlck.release()
    print()


def main(*args):
    try:
        arr = [1, 3, 5, 7, 9, 11]
        startTime = time.time()
        
        # Create thread
        t1 = threading.Thread(target=squares, args=(arr,))
        t2 = threading.Thread(target=cubes, args=(arr,))
        
        # Start thread
        t1.start()
        t2.start()
        
        # Wait
        t1.join()
        t2.join()
        
        endTime = time.time()
        
        print("Time required = ", endTime - startTime, 'sec')
        
        
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()


