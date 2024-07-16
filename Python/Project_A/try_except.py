def main():
    try:
        a = int(input("Enter an integer: "))
        b = int(input("Enter an integer: "))
        c = a/b
        print("c = ", c)

    except ValueError:
        print(ValueError)
        print(ValueError.args)

    except ZeroDivisionError as zde:
        print(zde)
        print(zde.args)

    except :
        print("Got Some Unexpected Error.")

    finally:
        print("I'm final block. I always run.")

if __name__ == '__main__':
    main()
