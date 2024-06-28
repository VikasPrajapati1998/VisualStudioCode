def main():
    try:
        student = {1: "Arjun", 2: "Bhola", 3: "Chitra", 4: "Dhanush", 5: "Elima", 6: "Faizal", 7: "Ganesh"}
        for k in student:
            print(k, end=", ")
        print()
        
        for k in student.keys():
            print(k, end=", ")
        print()
        
        for v in student.values():
            print(v, end=", ")
        print()
        
        for d in student.items():
            print(d, end=", ")
        print()
        
        for k, v in student.items():
            print(k, v)
        print()
    
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()

