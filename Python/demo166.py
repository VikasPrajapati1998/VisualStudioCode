import threading as td


class SquareGeneratorThread(td.Thread):
    def __init__(self):
        td.Thread.__init__(self)
    
    def run(self):
        print("Launching...")
    


def main(*args):
    try:
        th = SquareGeneratorThread()
        th.start()
    
    except Exception as e:
        print("main error : ", e)
        print(e.__annotations__)
    
    finally:
        print()


if __name__ == "__main__":
    main()
