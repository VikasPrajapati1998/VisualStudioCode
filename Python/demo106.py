def main(*args):
    try:
        path = "D:\\Programs\\VisualStudioCode\\Python\\Files\\"
        
        string = "Arjun Prajapati"
        tpl = ('Ajay', 23, 15000)
        lst = [23, 45, 56, 78, 90]
        dct = {"Name": "Dilip", "Age": 25}
        
        f = open(path+"text03.txt", 'w')
        f.write(string+"\n")
        f.write(str(tpl)+"\n")
        f.write(str(lst)+"\n")
        f.write(str(dct)+"\n")
        
        f.close()
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()
