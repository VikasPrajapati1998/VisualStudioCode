# Serialization and Deserialization

def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        
        # Write Files
        f = open(path+"text07.txt", "w")
        f.write(str(234)+"\n")
        f.write(str(13.45)+"\n")
        f.seek(0)
        f.close()
        
        # Read Files
        f = open(path+"text07.txt", "r")
        a = int(f.readline())
        b = float(f.readline())
        print("a = ", a)
        print("b = ", b)
        print("a + b = ", a + b)
        print("b + b = ", b + b)
        f.close()
    
    except Exception as e:
        print("main error : ", e)




if __name__ == "__main__":
    main()
