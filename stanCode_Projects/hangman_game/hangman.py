"""
File: hangman.py
Name: Mei Fei Chen
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO: To play hangman game.
    """
    n_turns = N_TURNS
    answer = random_word()
    dashed = ''
    for i in range(len(answer)):
        dashed += '-'

    correct_guess = ''
    while True:
        if dashed != answer:
            print(f'The word looks like: {dashed}')
            print(f'You have {n_turns} gusses left.')
            guess = input('Your guess: ').upper()       # case-insensitive

            while len(guess) != 1 or not guess.isalpha():
                print('illegal format.')
                guess = input('Your guess: ').upper()

            if guess in answer:     # if the guess is right
                dashed = ''
                print('You are correct!')
                correct_guess += guess
                for i in answer:
                    if i == guess or i in correct_guess:
                        dashed += i
                    else:
                        dashed += '-'
            else:                   # if guessed wrong
                n_turns -= 1
                print(f'There is no {guess}\'s in the word.')
                if n_turns == 0:
                    print('You are completely hung : (')
                    break
        else:
            print('You win!!')
            break

    print(f'The word was: {answer}')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
