
def main(*args):
    try:
        fruits = ["apple", "banana", "orange", "grape", "lemon"]
        reverse_fruits = list(reversed(fruits))
        print(fruits)
        print(reverse_fruits)
    
    except Exception as e:
        print("main error : ", e)
    


if __name__ == "__main__":
    main()


