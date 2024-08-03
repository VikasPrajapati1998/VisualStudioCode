# Read / Write Operations


def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        msg = "Bad officials are elected by good citizens who do not vote.\n"
        msgs = ["Humpty\n", "Dumpty\n", "Sat\n", "On\n", "a\n", "Wall\n"]
        
        # f = open(path+"text02.txt", "r")
        f = open(path+"text02.txt", "w")
        f.write(msg)
        f.writelines(msgs)
        f.close()
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()
