
# Logic 01 Not Using function
def main():
    stone = 20
    k = 1
    print("There are "+str(stone)+" stones left")
    try:
        while stone>0:
            player = int(input("Player " + str(k) + " would you like to remove 1 or 2 stones? "))
            while player<1 or player>2:
                player = int(input("Please enter 1 or 2: "))
            stone-=player
            print()
            if k==1:
                k=2
            else:
                k=1

            if stone<0:
                stone=0

            if stone>0:
                print("There are " + str(stone) + " stones left")

        print("Player " + str(k) + " wins!")

    except ValueError:
        print()
        print("You entered character or real value, program need only integer value.")
        print("Program will restart......!")
        print()
        main()
        return StopIteration

if __name__ == "__main__":
    main()
