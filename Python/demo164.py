def main(*args):
    try:
        import threading as td
        
        t = td.current_thread()  # return current thread object
        print("current thread : ", t)
        print("thread name : ", t.name)
        print("thread identifier : ", t.ident)
        print("is thread alive : ", t.is_alive())
        t.name = "My_Thread"
        print("After name change : ", t.name)
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()


if __name__ == "__main__":
    main()
