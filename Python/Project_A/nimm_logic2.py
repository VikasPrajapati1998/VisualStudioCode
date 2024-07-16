"""
TODO: Write a description here
"""
import random

def main():
    stones = 20  # start with total number of stones available
    print("There are " + str(stones) + " stones left")  # print the number of stones available at the beginning
    k = 1 # set the player counter; k can carry the values '1' or '2' only
    while stones != 0:  # set the while condition; the condition is that the number of stones must not be zero
        player = int(input("Player " + str(k) + " would you like to remove 1 or 2 stones? "))  # ask the player to remove a few stones
        while player < 1 or player > 2:  # check if the user input is legitimate and allowed, i.e., its value must be either 1 or 2, no more no less
            player = int(input("Please enter 1 or 2: "))  # request until the user supplies a valid value
        stones = stones - player  # remove the user specified value from the stones 'total'
        if stones > 1:
            print("\nThere are " + str(stones) + " stones left")
        if k == 1:  # switch to the next player, if the current player was player1, switch to player2
            k = 2
        elif k == 2:  # switch to the next player, if the current player was player2, switch to player1
            k = 1
    print("\nPlayer " + str(k) + " wins!")

if __name__ == '__main__':
    main()
