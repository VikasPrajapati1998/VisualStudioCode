# File Input / Output
"""_summary_: File Input Output

Args:
    *args: Variable Length Positional Arguments

Returns:
    Any: None
"""

def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        # data
        msg1 = "Pay taxes with a smile...\n"
        msg2 = "I tried, but they wanted money!\n"
        msg3 = "Don't feel bad...\n"
        msg4 = "It is alright to have no talent!\n"
        
        # Write in file.
        f = open(path+"text01.txt", "w")
        f.write(msg1)
        f.write(msg2)
        f.write(msg3)
        f.write(msg4)
        f.close()
        
        # Read from file.
        f = open(path+"text01.txt", "r")
        data = f.read()
        print(data)
        f.close()
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()

