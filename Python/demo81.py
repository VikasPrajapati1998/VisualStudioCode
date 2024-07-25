# iterator

def main(*args):
    try:
        string = "Prajapati"
        lst = ['Focussed', 'bursts', 'of', 'activity']
        print(hasattr(string, '__iter__'))
        print(hasattr(string, '__next__'))
        print(hasattr(lst, '__iter__'))
        print(hasattr(lst, '__next__'))
        print()
        
        it_string = iter(string)
        it_list = iter(lst)
        print(hasattr(it_string, '__iter__'))
        print(hasattr(it_string, '__next__'))
        print(hasattr(it_list, '__iter__'))
        print(hasattr(it_list, '__next__'))
        print()
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()

