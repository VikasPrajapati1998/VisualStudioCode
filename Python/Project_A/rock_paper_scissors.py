"""
Implements the game of Rock-Paper-Scissors!

History:
This classic game dates back to the Han Dinesty, over 2200 years ago.
The First International Rock-Paper-Scissors Programming Competition
was held in 1999 and was won by a team called "Iocaine Powder"

The Game:
Each player chooses a move (simultaneously) from the choices:
rock, paper or scissors.
If they chose the same move the game is a tie. Otherwise:
rock beats scissors
scissors beats paper
paper beats rock.

In this program a human plays against an AI. The AI chooses randomly
(we promise). The game is repeated N_GAMES times and the human gets
a total score. Each win is worth +1 points, each loss is worth -1
1. Rock beat Scissors
2. Scissors beat Paper
3. Paper beat Rock
"""
import random

N_GAMES = 3
score = 0

def main():
    global score
    print_welcome()
    for i in range(3):
        ai_move = get_ai_move()
        human_move = get_human_move()
        outcome = decide_outcome(ai_move, human_move)

        print("The AI plays: ", ai_move)
        print("The winner is: ", outcome)

        score = calc_outcome_score(outcome)
    print("Score = ", score)

def calc_outcome_score(outcome):
    global score
    if outcome == "human":
        score += 1
        return score
    if outcome == "ai":
        score -= 1
        return score
    if outcome == "tie":
        score += 0
        return score

def decide_outcome(ai_move, human_move):
    if ai_move == human_move:
        return "tie"
    elif ai_move == "rock":
        if human_move == "scissors":
            return "ai"
        else:
            return "human"
    elif ai_move == "paper":
        if human_move == "scissors":
            return "human"
        else:
            return "ai"
    elif ai_move == "scissors":
        if human_move == "rock":
            return "human"
        else:
            return "ai"

def get_ai_move():
    ai = random.randint(1, 3)
    if ai==1:
        return 'rock'
    elif ai==2:
        return 'scissors'
    else:
        return 'paper'

def get_human_move():
    human = input('What do you play? ')
    while not(is_valid_move(human)):
        print('Invalid Input  please try again.')
        human = input('What do you play? ')
    return human

def is_valid_move(human):
    if human=="rock":
        return True
    elif human=="paper":
        return True
    elif human=="scissors":
        return True
    else:
        return False

def print_welcome():
    print('Welcome to Rock Paper Scissors')
    print('You will play '+str(N_GAMES)+' games against the AI')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    print('----------------------------------------------')
    print('')

if __name__ == '__main__':
    main()
