def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        f = open(path+"text04.txt", "r+")
        while True:
            data = f.readline()
            if data == '':
                break
            print(data, end='')
                
        f.close()
                
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()


