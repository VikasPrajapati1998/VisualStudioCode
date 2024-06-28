# --------- dictionary -------------- 

def main():
    try:
        dtc = {"Amit": 47, "Ankit": 67, "Aman": 98, "Ankur": 89, "Bhavna": 73, "Chitra": 92}
        # dictionary methods
        var = dtc.get("Ankur", "Absent")
        print(var)
        var = dtc.get("Kiran", "Absent")
        print(var)
        k = dtc.keys()
        print(k)
        v = dtc.values()
        print(v)
        print(dtc)
        dtc["Dhiraj"] = 81
        print(dtc)
        print(dtc["Aman"])
        dtc["Pawan"] = 76
        print(dtc)
        
        # update
        dtc1 = {"Elimma": 65, "Faizal": 87, "Ganesh": 75, "Harshit": 83, "Irish": 72, "Julie": 67}
        dtc.update(dtc1)
        print(dtc)
        
        # popitem
        print(dtc.popitem()) # remove from last
        print(dtc.pop("Elimma")) # remove key-value and return value
        print(dtc)
        dtc.clear()
        print(dtc)
        
        # create dictionary
        lst = ["Alpah", "Beta", "Chalu", "Delta", "Eta", "Femta", "Gama", "Hecta", "Jitter"]
        d = dict.fromkeys(lst, 50)
        print(d)
    
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()



