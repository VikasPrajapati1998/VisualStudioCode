import sys, operator


def main(*args):
    try:
        var = int(input("Enter a number : "))
        print("Squire of number : ", (lambda x: x*2)(var))
        name = input("Enter your name : ")
        print("Sure Name : Mr/Ms", (lambda n: n.split(" "))(name)[-1].capitalize())
        
        dct = {'Oil': 230, 'Clip': 150, 'Stud': 175, 'Nut': 35}
        d1 = sorted(dct.items(), key=lambda kv: kv[0])
        print(d1)
        d2 = sorted(dct.items(), key=lambda kv: kv[-1])
        print(d2)
        d3 = sorted(dct.items(), key=operator.itemgetter(0))
        print(d3)
        d4 = sorted(dct.items(), key=operator.itemgetter(1))
        print(d4)
        
    
    except Exception as e:
        print("main error :", e)
        

if __name__ == "__main__":
    main()
