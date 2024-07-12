def count_alpha_digit(string):
    dct = {"Digits": 0, "Alphabets": 0, "Special Character": 0}
    for char in string:
        if char.isalpha():
            dct['Alphabets'] += 1
        elif char.isdigit():
            dct["Digits"] += 1
        else:
            dct["Special Character"] += 1
            
    return(dct)


def main(*args) :
    try:
        dct = count_alpha_digit("James Bond 007")
        print(dct)
        
        st = "Kohli Number 420"
        dct = count_alpha_digit(st)
        print(dct)
        
    
    except Exception as e:
        print("Main Error : ", e)
    
    

if __name__ == "__main__":
    main()
