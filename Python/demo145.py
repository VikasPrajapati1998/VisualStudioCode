def main(*args):
    try:
        import os
        
        # code chunk 1
        print("================ code chunk 1 ===============")
        entries = os.listdir("Python//my_directory/")
        for dir in entries:
            print(dir)
        print()
        
        # code chunk 2
        print("================ code chunk 2 ===============")
        entries = os.scandir("Python//my_directory/")
        for dir in entries:
            print(dir)
        print()
        
        # code chunk 3
        print("================ code chunk 3 ===============")
        with os.scandir("Python//my_directory/") as entries:
            for entry in entries:
                print(entry.name)
            print()
        
        # code chunk 4
        print("================ code chunk 4 ===============")
        from pathlib import Path
        
        entries = Path("Python//my_directory/")
        for entry in entries.iterdir():
            print(entry.name)
        print()
        
        # code chunk 5
        print("================ code chunk 5 ===============")
        basepath = Path("Python//my_directory/")
        # List all files in a directory using os.listdir
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                print(entry)
        print()
        
        # code chunk 6
        print("================ code chunk 6 ===============")
        basepath = Path("Python//my_directory/")
        # List all files in a directory using os.listdir
        for entry in os.listdir(basepath):
            if os.path.isdir(os.path.join(basepath, entry)):
                print(entry)
        print()
        
        # code chunk 7
        print("================ code chunk 7 ===============")
        # List all files in directory using pathlib
        basepath = Path("Python//my_directory/")
        files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
        for item in files_in_basepath:
            print(item.name)
        print()
        
        # code chunk 8
        print("================ code chunk 8 ===============")
        '''
        os.remove() : Deletes a file and does not delete directories
        os.unlink() : Is identical to os.remove() and deletes a single file
        pathlib.Path.unlink(): Deletes a file and cannot delete directory
        
        os.rmdir() : Delete an empty directory
        pathlib.Path.rmdir() : Delele an empty directory
        shutil.rmtree() : Deletes entire directory tree and can be used to delete not empty directories.
        '''
            
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()




if __name__ == "__main__":
    main()

