# serialize / deserialize 
import json


def main(*args):
    try:
        lst = [x*10 for x in range(1, 10)]
        tpl = ("Arjun", 23, 2456.78)
        dct = {"Anil": 26, "Siksha": 23, "Arjun": 25, "Jiya": 22, }
        
        str1 = json.dumps(lst)
        str2 = json.dumps(tpl)
        str3 = json.dumps(dct)
        
        l = list(json.loads(str1))
        t = tuple(json.loads(str2))
        d = dict(json.loads(str3))
        
        print("list : ", l)
        print("tuple : ", t)
        print("dictionary : ", d)
        print()
        
    except Exception as e:
        print("main error : ", e)




if __name__ == "__main__":
    main()


