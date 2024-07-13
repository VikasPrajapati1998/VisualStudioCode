def show(*args):
    try:
        for item in args:
            print(item)
    
    except Exception as e:
        print("myModule show error : ", e)

def welcome():
    print("Welcome to the world of programming.")


def main(*args):
    try:
        welcome()
        show("Arjun Prajapati")
        show(23)
    
    except Exception as e:
        print("myModule main error : ", e)


if __name__ == "__main__":
    main()
