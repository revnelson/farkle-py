#!/usr/bin/env python

from random import randint

# Verification functions and point calculation
from verify import *


scoreboard = {}  # Keep track of players' scores
order = []  # Maintain order of players as input


# Input player's names and create scoreboard
def players():
    for i in range(verify_players()):
        name = input("Player %s's name: " % (i+1))  # TODO Check input for error
        while True:
            if name not in scoreboard:
                scoreboard[name] = 0
                order.append(name)
                break
            else:
                name = input("%s has already been added to the game.\nPlease give player %s a unique name: "
                             % (name, i+1))  # TODO Check input for errors
    return scoreboard


# Roll n number of dice
def roll(n):
    return [str(randint(1, 6)) for _ in range(n)]


# Play hand
def hand(player, score):
    dice = 6
    set_aside = []  # Dice set aside

    while True:

        current_roll = roll(dice)
        print("You just rolled:\n%s\n" % ' '.join(current_roll))

        # Verify roll has value and check if all-dice
        verified_roll = point_count([], current_roll)
        if len(verified_roll[1]) is 0:
            print("Congratulations, you get to roll them all again!")
            return [point_count(set_aside, current_roll)[0], 'all']
        if verified_roll[0] > 0:

            # If current roll has value
            print(point_count(set_aside, current_roll)[0])  # TODO Be more informative about scoring

            while True:

                action = verify_user_input()  # Ask player what they want to do

                if action == 1:

                    keep = verify_keep(current_roll)  # Keep some dice

                    set_aside.append(keep)  # Add kept dice to list

                    dice -= len(keep)  # Update number of dice available to roll

                    break

                else:
                    # End turn and keep points
                    hand_result = point_count(set_aside, current_roll)
                    if scoreboard[player] < 1000 and hand_result[0] + score < 1000:  # Check for min score for stopping
                        print("You must end your turn with at least 1000 points to get on the board.\n")
                    else:
                        return hand_result[0], 'done'  # End hand as well as turn
        else:
            print("Sorry, you didn't roll any points.")
            return [0, 'fail']  # If no points rolled, end turn with no points


# TODO Create turn system in order

# Starts the turn
def turn(player):

    score = 0

    while True:

        hand_result = hand(player, score)  # Passes name and accumulated turn score, returns points and ending reason

        score += hand_result[0]

        if hand_result[1] is 'done':  # Finished turn and adds points to scoreboard if player successful
            scoreboard[player] += score
            print(scoreboard)
            break

        elif hand_result[1] is 'fail':  # Finishes turn with no points if player failed
            print(scoreboard)
            break

        print("Your score for this turn so far is:\n%s" % score)  # Loops if all dice in hand had value

# TODO Make last turn scenario
players()
print(turn('John'))
