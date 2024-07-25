import re

def main(*args):
    try:
        s1 = "foo123bar"
        print('123' in s1)
        print(s1.find("123"))
        print(s1.index("123"))
        print(re.search("123", s1))
        print(re.search("3b", s1))
        print()
        
        s2 = 'Arjun@191198#Prajapati'
        print(s2.find("1911")) 
        print(re.search("1911", s2)) 
        print(re.search("[0-9][0-9][0-9][0-9]", s2)) 
        print(re.search("1911", s2)) 
        print() 
        
        s3 = "foo123fun456bar"
        print(re.search('1.3', s3)) 
        print(re.search('4.6', s3))  
        print() 
        
        s4 = "Arjun12345Prajapati6789"
        print(re.search("6.8", s4))
        print()
        
        
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()

