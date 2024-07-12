# list, tuple, set dictionary
import operator

def main():
    try:
        dct = {'Oil': 230, 'Clip': 150, 'Stud': 175, 'Nut': 35}
        print('Original Dictionary : ', dct)
        
        # sorting by key
        dct1 = sorted(dct.items())
        print('Asc. order by key : ', dct1)
        dct2 = sorted(dct.items(), reverse=True)
        print('Des. order by key : ', dct2)
        
        # sorting by value
        dct1 = sorted(dct.items(), key=operator.itemgetter(1))
        print('Asc. order by value : ', dct1)
        dct2 = sorted(dct.items(), key=operator.itemgetter(1), reverse=True)
        print('Des. order by key : ', dct2)
    
    except Exception as e:
        print("Error : ", e)


if __name__ == "__main__":
    main()


