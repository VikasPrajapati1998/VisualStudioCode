# buit-in Functions on Dictionary
import operator

def main(lst=None):
    try:
        dtc = {'Amit': 47, 'Ankit': 67, 'Aman': 98, 'Ankur': 89, 'Bhavna': 73, 'Chitra': 92, 'Dhiraj': 81,\
            'Pawan': 76, 'Elimma': 65, 'Faizal': 87, 'Ganesh': 75, 'Harshit': 83, 'Irish': 72, 'Julie': 67}
        
        print(dtc)
        print(len(dtc))
        print(max(dtc))
        print(min(dtc))
        print(sorted(dtc))
        print(sorted(dtc, reverse=True))
        print(sum(dtc.values()))
        print(any(dtc))
        print(all(dtc))
        print(dict(reversed(dtc.items())))
        print(operator.itemgetter(1))
        
    
    except Exception as e:
        print(e)
        

if __name__ == "__main__":
    main()

