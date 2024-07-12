import operator, random

def main(*args):
    try:
        s1 = 'dreams may change, but friends are forever'
        print(s1.split())
        s2 = [' '.join(w.capitalize() for w in s1.split())]
        print(*s2)
    
    except Exception as e:
        print(e)
        
        

if __name__ == "__main__":
    main()
