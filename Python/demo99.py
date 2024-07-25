import re

def main(*args):
    try:
        # Regexes in Python and Their Uses
        string = 'foo123bar'
        print('123' in string)
        
        print(string.find('123'))
        print(string.index('123'))
        
        print(re.search('123', string))
        
        if re.search('123', string):
            print('Found a match.')
        else:
            print('No match.')
        
        print(string[3:6])
        
        print(re.search('[0-9][0-9][0-9]', 'foo123bar'))
        print(re.search('[0-9][0-9][0-9]', 'foo456bar'))
        print(re.search('[0-9][0-9][0-9]', '234baz'))
        print(re.search('[0-9][0-9][0-9]', 'qux678'))
        print(re.search('[0-9][0-9][0-9]', '123foo456'))
        print()
        
        print(re.search('1.3', 'foo123bar'))
        
        email = "vikas191198@gmail.com"
        print(email)
        print(re.search('1911', email))
        print(re.search('[a-z]', 'FOObar'))
        print(re.search('ba[artz]', 'foobarqux'))
        print(re.search('[0-9][0-9]', 'foo123bar'))
        
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()

