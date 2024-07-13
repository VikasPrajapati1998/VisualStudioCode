def display(*args):
    try:
        for val in args:
            print(val)
        
    except Exception as e:
        print("myModule02 display error : ", e)


display("This is the module 2.")