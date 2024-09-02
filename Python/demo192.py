# Semaphore
import threading as th
import time

sem = th.BoundedSemaphore(3)

def fun(msg):
    sem.acquire()
    t = th.current_thread()
    while True:
        print(t.name, ":", msg)
    sem.release()
    time.sleep(1)
    


def main(*args):
    try:
        th1 = th.Thread(target=fun, args=("Arjun",))
        th2 = th.Thread(target=fun, args=("Sudhanshu",))
        th3 = th.Thread(target=fun, args=("Vishal",))
        th4 = th.Thread(target=fun, args=("Madhvi",))
        
        th1.start()
        th2.start()
        th3.start()
        th4.start()
        
        th1.join()
        th2.join()
        th3.join()
        th4.join()
    
    except Exception as e:
        print("main error ", e)
    
    

if __name__ == "__main__":
    main()

