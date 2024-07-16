import time
start_time = time.time()
print("Timer has started")
i=0
while i<60:
    print("Timer elapsed=:", round(time.time()-start_time, 0), 'secs', end='\n')
    time.sleep(1)
    i+=1
