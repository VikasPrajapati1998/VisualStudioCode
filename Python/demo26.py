import operator

def main():
    try:
        lst = [("Amit", 24, 56999.50), ("Bindu", 22, 45000.00), ("Charan", 26, 33000), ("Dinesh", 21, 28000), ("Ekta", 24, 43000.54)]
        print(sorted(lst))
        print(sorted(lst, key=operator.itemgetter(1)))
        print(sorted(lst, key=operator.itemgetter(2)))
        print(sorted(lst, key=operator.itemgetter(2), reverse=True))
        
        dct = {"Sunil": 20, "Sachin": 50, "Rahul": 10, "Kapil": 30, "Sushil": 40, "Ritesh": 60}
        print(dct)
        
        d1 = sorted(dct.items(), key=operator.itemgetter(1))
        print(d1)
        
        d2 = sorted(dct.items(), key=operator.itemgetter(1), reverse=True)
        print(d2)
        
        
    except Exception as e:
        print(e)
    
    finally:
        print()


if __name__ == "__main__":
    main()




