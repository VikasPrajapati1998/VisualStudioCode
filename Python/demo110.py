def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        with open(path+"text06.txt", "r+", encoding="utf-8") as f:
            while True:
                data = f.readline()
                if data == '':
                    break
                print(data, end='')
        print()
        
        with open(path+"text06.txt", "r+", encoding="utf-8") as f:
            try:
                data = f.read(101); print(data, end=''); print()
                
                f.seek(0)
                data = f.read(89); print(data, end=''); print()
                
                f.seek(48, 0)
                data = f.read(40); print(data, end=''); print()
                print()
                
                print("================================ f.seek(1) =================================")
                f.seek(100, 0)
                f.seek(-10, 1)
                data = f.read(50); print(data, end=''); print()
                
            
            except Exception as e:
                print("file error : ", e)
            
            
    except Exception as e:
        print("main erro : ", e)
    
    finally:
        print()


if __name__ == "__main__":
    main()


