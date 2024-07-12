def convert(str1):
    items = [s for s in str1.split('-') ]
    items.sort()
    str2 = '-'.join(items)
    return str2

def convert_string(st):
    words = [word for word in st.split(' ')]
    s = ' '.join(sorted(list(set(words))))
    return s
    

def main(*args) -> None :
    try:
        s = 'here-come-the-dots-followed-by-dashes'
        t = convert(s)
        print(t)
        
        s = "I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn\'t really happy"
        t = convert_string(s)
        print(t)
        
        s = "Sakhi was a singer because her mother was a singer, and Sakhi\'s mother was a singer because her father was a singer"
        t = convert_string(s)
        print(t)
    
    except Exception as e:
        print("Main Error : ", e)


if __name__ == "__main__":
    main()

