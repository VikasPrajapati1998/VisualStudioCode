'''
_______________________________________________________________________________________________________________
Concurrency: In Python, the things that are occurring simultaneously are called by different 
names (thread, task, process) but at a high level, they all refer to a sequence of instructions
that run in order.

Note: Only multiprocessing actually runs these trains of thought at literally the same time.
Threading and asyncio both run on a single processor and therefor only run one at a time.
_______________________________________________________________________________________________________________

_______________________________________________________________________________________________________________
Threading: In threading, the operating system actually knows about each thread and can interrupt it at any 
time to start running a different thread. This is called pre-emptive multitasking since the 
operating system can pre-empt your thread to make the switch.
Pre-emptive multitasking is handy in that the code in the thread doesn’t need to do anything to 
make the switch. It can also be difficult because of that “at any time” phrase. This switch can 
happen in the middle of a single Python statement, even a trivial one like x = x + 1.

Asyncio: Asyncio, on the other hand, uses cooperative multitasking. The tasks must cooperate by announcing 
when they are ready to be switched out. That means that the code in the task has to change slightly 
to make this happen.
The benefit of doing this extra work up front is that you always know where your task will be swapped 
out. It will not be swapped out in the middle of a Python statement unless that statement is marked. 
You’ll see later how this can simplify parts of your design.
_______________________________________________________________________________________________________________

_______________________________________________________________________________________________________________
Multiprocessing: With multiprocessing, Python creates new processes. A process here can be thought
of as almost a completely different program, though technically they’re usually defined as a collection
of resources where the resources include memory, file handles and things like that. One way to think 
about it is that each process runs in its own Python interpreter.
Because they are different processes, each of your trains of thought in a multiprocessing program can 
run on a different core. Running on a different core means that they actually can run at the same time, 
which is fabulous. There are some complications that arise from doing this, but Python does a pretty 
good job of smoothing them over most of the time.
_______________________________________________________________________________________________________________
'''

'''
 ____________________________________________________________________________________________________________________________________________
|            Concurrency Type            |                            Switching Decision                         |   Number of Processors    |
|________________________________________|_______________________________________________________________________|___________________________|
|Pre-emptive Multitasking (threading)    |  The operating system decides when to switch tasks external to Python.|               1           |
|________________________________________|_______________________________________________________________________|___________________________|
|Cooperative Multitasking (asyncio)      |  The tasks decide when to give up control.                            |               1           |
|________________________________________|_______________________________________________________________________|___________________________|
|Multiprocessing                         |  The process all run at the same time on different processors.        |              Many         |
|________________________________________|_______________________________________________________________________|___________________________|

'''

'''
# I/O-Bound Process:
    1. Your program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer.
    2. Speeding it up involves overlapping the times spent waiting for these devices.

# CPU-Bound Process:
    1. Your program spends most of its time doing CPU operations.
    2. Speeding it up involves finding ways to do more computations in the same amount of time.
'''
def main(*args):
    try:
        pass
    
    except Exception as e:
        print("main error : ", e)
        print(e.__annotations__)


if __name__ == "__main__":
    main()
