def main():
    try:
        s = {12, 15, 13, 23, 22, 16, 17}
        t = {'A', 'B', 'C'}
        u = set()   # empty set
        s.add("Hello")  # adds "Hello" to s
        s.update(t)     # adds elements of t to s
        print(s)

        u = s.copy()
        s.remove(15)    # delete 15 from s
        print(s)
        # s.remove(101)   # remove 101 from s
        print(s)
        s.discard(12)   # remove 12 from s
        print(s)
        s.discard(101)  # won't raise an error, though 101 is not in s
        print(s)
        s.clear()   # removes all elements
        print(u)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()


