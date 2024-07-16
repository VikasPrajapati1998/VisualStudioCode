def main():
    n = int(input('Number to count to: '))
    fizz = 0
    buzz = 0
    fizzbuzz = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz += 1
            print('Fizzbuzz')
        elif i % 3 == 0:
            print('Fizz')
            fizz += 1
        elif i % 5 == 0:
            print('Buzz')
            buzz += 1
        else:
            print(i)
    print('')
    print('Num fizzed: ', fizz)
    print('Num buzzed: ', buzz)
    print('Num fizzbuzzed: ', fizzbuzz)

if __name__=='__main__':
    main()
