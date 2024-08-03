def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        f = open(path+"text04.txt", "w+")
        while True:
            data = input("Enter the message : ")
            f.writelines(data)
            f.write("\n")
            if data == '':
                break
        
        f.close()
                
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()


