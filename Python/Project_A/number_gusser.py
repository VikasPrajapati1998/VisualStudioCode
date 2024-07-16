"""
Number Guesser Prograam

This is an example of how to use variables to
keep track of information in a program that
also makes use of loops
"""
import random

MIN = 0
MAX = 100

def main():
    count = 0
    lower_limit = MIN
    upper_limit = MAX

    while True:
        count += 1
        guess = random.randint(lower_limit, upper_limit)

        user_response = input("Is your number " + str(guess) + "?")

        if user_response == 'higher':
            upper_limit = guess
        if user_response == 'lower':
            lower_limit = guess
        if user_response == 'correct':
            break

    print("I win! It took me " + str(count) + " guesses")


if __name__ == "__main__":
    main()
