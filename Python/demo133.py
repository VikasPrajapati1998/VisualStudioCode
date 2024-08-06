def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        with open("file.log") as file:
            read_data = file.read()
            print(read_data)
    
    
    except FileNotFoundError as fnf:
        print("File Not Found Error : ", fnf)
    
    except RuntimeError as rte:
        print("Runtime error : ", rte)
    
    except Exception as e:
        print("main error : ", e)
    
    else:
        print("No Error Found.")
    
    finally:
        print("Program End")
        print()



if __name__ == "__main__":
    main()

