# Serialize / Deserialize nested list
import json


def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        
        list_of_list = [10, [20, 30, 40], [50, 60, 70], 80, 90]
        with open(path+"text11.txt", "wt+") as file:
            # serialize
            json.dump(list_of_list, file)
            file.seek(0)

            # deserialize
            data = json.load(file)
            print(data)
        
        contacts = {
                        "Anil": {'DOB': '17/11/1998', 'Favorite': 'Igloo'},
                        "Anmol": {'DOB': '14/10/1999', 'Favorite': 'Tundra'},
                        "Ravi": {'DOB': '19/11/1997', 'Favorite': 'Artic'}
                    }
        with open(path+"text12.txt", "wt+") as file:
            # serialize
            json.dump(contacts, file)
            file.seek(0)
            
            # deserialize
            data = json.load(file)
            print(data)
        
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print("Program End...!")



if __name__ == "__main__":
    main()

