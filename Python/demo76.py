def main(*args):
    try:
        words = ['A', 'coddle', 'called', 'Molly']
        numbers = [10, 20, 30, 40]

        for ele in zip(words, numbers):
            print(ele[0], ':', ele[1])
        print()

        for ele in zip(words, numbers):
            print(ele)
        print()

        for w, n in zip(words, numbers):
            print(w, ':', n)
        print()

    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()


