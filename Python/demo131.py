
def main(*args):
    try:
        import datetime
        
        today = datetime.datetime.now()
        print(today)
        print()
        print("================================ str ==============================")
        print(str(today))
        print(format(today))
        print("{}".format(today))
        print("{!s}".format(today))
        print()
        print(f"{today}")
        print(f"{today!s}")
        print(f"{today = !s}")
        print()
        
        print("=============================== repr ===============================")
        print(repr(today))
        print(format(repr(today)))
        print("{}".format(repr(today)))
        print("{!r}".format(today))
        print()
        print(f"{repr(today)}")
        print(f"{today!r}")
        print(f"{today = !r}")
        
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()



if __name__ == "__main__":
    main()

