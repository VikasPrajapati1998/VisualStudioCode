def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        # with open(path+"text05.txt", "w") as f:
        #     while True:
        #         data = input("Enter message : ")
        #         if data == '':
        #             break
        #         f.writelines(data+"\n")
        # print()
        
        with open(path+"text05.txt", "r") as f:
            while True:
                data = f.readline()
                if data == '':
                    break
                print(data, end='')
        print()
            
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()


