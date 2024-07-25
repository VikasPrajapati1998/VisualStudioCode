def main(*args):
    try:
        words = ['A', 'B', 'C', 'D']
        numbers = [1, 2, 3, 4]
        for ele in zip(words, numbers):
            print(ele)
        print()
        
        for ele in zip(words, numbers):
            print(*ele)
        print()
        
        for ele in zip(words, numbers):
            print(ele[0], ':', ele[1])
        print()
        
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()


