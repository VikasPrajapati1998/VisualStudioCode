import threading as th

def fun(var):
    print("Hello World...")

var = 2
t1 = th.Thread(target=fun, args=(var,), name="Th1")

t1.start()
t1.join()

