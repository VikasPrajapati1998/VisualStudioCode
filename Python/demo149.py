
def main(*args):
    try:
        dct = {"Arjun": 123, "Mohan": 456, "Vikas": 76, "Akash": 89, "Himanshu": 98}
        for x in dct.items():
            y = x[-1]
            l = lambda k: k+k
            print(f"{x[0]}: {l(y)}")
        
    
    except Exception as e:
        print("main error :" , e)


if __name__ == "__main__":
    main()



