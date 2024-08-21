import threading
import time

def fun1():
    t = threading.current_thread()
    print(f"Starting {t.name}")
    time.sleep(1)
    print(f"Exiting {t.name}")

def fun2():
    t = threading.current_thread()
    print(f"Starting {t.name}")
    time.sleep(1)
    print(f"Exiting {t.name}")
    
def fun3():
    t = threading.current_thread()
    print(f"Starting {t.name}")
    time.sleep(1)
    print(f"Exiting {t.name}")


def main(*args):
    try:
        t1 = threading.Thread(name="Thread-1", target=fun1)  # use default name
        t2 = threading.Thread(name="Thread-2", target=fun2)
        t3 = threading.Thread(name="Thread-3", target=fun3)
        
        t1.start()
        t2.start()
        t3.start()
    
    except Exception as e:
        print("main error : ", e)
        
    finally:
        print()
    
    
if __name__ == "__main__":
    main()
