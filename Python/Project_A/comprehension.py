def main():
    # Greater number
    x = int(input('Enter x : '))
    y = int(input('Enter y: '))
    s = x if (x > y) else y
    print(s)
    print()
    # pass, break and continue statement
    for i in range(25):
        if i==10: break
        if i==5: continue
        if i==3: pass
        print(i)
    print()
    # enumerator function
    lst = ['Ajay', 'Vijay', 'Suraj', 'Rohit', 'Sumit', 'Kapil']
    for i in lst:
        print(i)
    print()
    for i, j in enumerate(lst):
        print(i, j)
    print()

if __name__ == '__main__':
    main()
