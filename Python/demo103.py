if __name__ == "__main__":
    import sys
    print("Number of arguments received : ", len(sys.argv))
    print("Arguments received : ", str(sys.argv))
    print()
    
    for args in sys.argv:
        print(args, sep = ", ")
    print()



