def func1():
    print("func1")

def func2():
    print("func2")

def main(*args):
    '''Method 01 : By passing the name of the function that should run as a separate thread, to the constructor of the Thread class.'''
    try:
        import threading as td
        
        # create threads
        th1 = td.Thread(name="my first thread", target=func1)
        th2 = td.Thread(target=func2)
        
        # shoot/start the thread
        th1.start()
        print(th1.name, th1.ident)
        
        th2.start()
        print(th2.name, th2.ident)
        
        
    
    except Exception as e:
        print("main error : ", e)
        print(e.__getattribute__)
        print("_________________________________________")
        print(e.__annotations__)
    
    finally:
        print()



if __name__ == "__main__":
    main()
