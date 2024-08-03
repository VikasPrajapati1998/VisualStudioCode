# serialize / deserialize a list

import json

def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        
        # dump and load the list
        with open(path+"text08.txt", "w+") as file:
            lst = [x*10 for x in range(1, 10)]
            
            # serialize
            json.dump(lst, file)
            file.seek(0)
            
            # deserialize
            load_list = json.load(file)
            print(load_list)
        
        
        # dump and load the tuple
        with open(path+"text09.txt", "w+") as file:
            tpl = ("Arjun", 23, 2455.55)

            # serialize
            json.dump(tpl, file)
            file.seek(0)
            
            # deserialize
            load_tuple = json.load(file)
            print(load_tuple)
        
        
        # dump and load the dictionary
        with open(path+"text10.txt", "w+") as file:
            dct = {"Anil": 24, "Ajay": 23, "Nisha": 22}
            
            # serialize
            json.dump(dct, file)
            file.seek(0)
            
            # deserialize
            load_dict = json.load(file)
            print(load_dict)
            
    
    except Exception as e:
        print("main error : ", e)




if __name__ == "__main__":
    main()

