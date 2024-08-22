def main(*args):
    file_path = "Files/analysis_data190.json"  # Ensure the path is correct

    try:
        with open(file_path, "r") as file:
            data = file.read()
            print(data)
        
        # # Open the file in read mode
        # with open(file_path, 'r') as file:
        #     while True:
        #         line = file.readline()
        #         if line == '':  # Check for end-of-file
        #             break
        #         # Print or process the line
        #         print(line.strip())  # Use strip() to remove leading/trailing whitespace, including newline
        
        # with open(file_path, 'r') as file:
        #     data = file.readlines()
        #     print(data)
                
    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: An I/O error occurred.")
    except Exception as e:
        print("An unexpected error occurred: ", e)
    
    finally:
        print("Finished processing the file.")

if __name__ == "__main__":
    main()
