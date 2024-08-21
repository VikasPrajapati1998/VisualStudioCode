# No Concurrency and Prallelism 

import time
import threading

def squares(nos):
    print("Calculating Squares : ")
    for n in nos:
        time.sleep(0.5)
        print('n = ', n, 'square = ', n*n)
    print()


def cubes(nos):
    print("Calculating Cubes : ")
    for n in nos:
        time.sleep(0.5)
        print('n = ', n, 'cube = ', n*n*n)
    print()


def main(*args):
    try:
        arr = [1, 3, 5, 7, 9, 11]
        startTime = time.time()
        squares(arr)
        cubes(arr)
        endTime = time.time()
        
        print("Time required = ", endTime - startTime, 'sec')
        
        
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()



