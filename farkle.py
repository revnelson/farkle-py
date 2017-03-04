#!/usr/bin/env python

from random import randint

# Verification functions
from verify import *


scoreboard = {}  # Keep track of players' scores
order = []  # Maintain order of players as input


# Input player's names and create scoreboard
def players():
    for i in range(verify_players()):
        name = input("Player %s's name: " % (i+1))
        while True:
            if name not in scoreboard:
                scoreboard[name] = 0
                order.append(name)
                break
            else:
                name = input("%s has already been added to the game.\nPlease give player %s a unique name: "
                             % (name, i+1))
    return scoreboard


# Roll n number of dice
def roll(n):
    return [str(randint(1, 6)) for _ in range(n)]


def keep_or_finish():
    selection = int(input("Please pick from the following options:\n1. Hold some dice and roll again.\n"
                          "2. End turn and keep points\n"))
    # TODO Add selection verification
    return selection


def hand():
    dice = 6
    # How many rolls this hand
    roll_count = 0
    # Dice set aside
    set_aside = {}
    while True:
        roll_count += 1
        current_roll = roll(dice)
        print(' '.join(current_roll))
        # Verify roll
        if verify_roll(current_roll, set_aside, roll_count):
            # Insert action selection
            action = keep_or_finish()
            if action == 1:
                # Keep some dice
                keep = verify_keep(current_roll)
                # Update number of dice available to roll
                dice -= len(keep)
                set_aside[roll_count] = keep
                if dice == 0:
                    print("Congratulations, you get to roll them all again!")
                    return [sum([x for x in set_aside.values()][0]), True]  # todo calculate real scores
            else:
                # End turn and keep points
                # todo make sure player has at least 1000 points to finish turn voluntarily
                set_aside[roll_count] = [int(x) for x in current_roll]
                return [sum([x for x in set_aside.values()][0]), False]  # todo calculate real scores
        else:
            print("Sorry, you didn't roll any points.")
            return [0, False]  # If no points rolled


# todo Create turn system in order
def turn(player):
    # Starts the turn
    while True:

        hand_result = hand()
        score = hand_result[0]
        if hand_result[1] is False:
            scoreboard[player] += score
            print(scoreboard)
            break

# todo Make last turn scenario
players()
print(turn('John'))
