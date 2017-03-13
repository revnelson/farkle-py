def verify_players():
    return int(input("How many players? "))  # TODO Check input for errors


# Gets verified choice of dice to keep from current roll
def verify_keep(set_aside, current_roll):

    keep = ''.join(input("Which would you like to hold? ").split())

    while True:

        if keep.isdigit():
            for i in keep:  # Reports error if player chooses dice that aren't in the current roll
                if keep.count(i) > current_roll.count(i):
                    keep = ''.join(input("Those weren't all in your roll.\n"
                                         "Please enter only numbers from your current roll of %s.\n"
                                         "Which would you like to hold? " % (' '.join(current_roll))).split())

        elif keep.isdigit() is False:  # Reports error if player inputs non-digits
            keep = ''.join(input("You entered non-numbers.\nPlease enter only numbers from your current roll of %s.\n"
                                 "Which would you like to hold? " % (' '.join(current_roll))).split())

        non_points = point_count(set_aside, [int(x) for x in keep])[1]

        if len(non_points) > 0:  # Ensures all dice kept have value
            keep = ''.join(input("The following dice have no value:\n%s\n"
                                 "Please select dice with value: " % (' '.join([str(x) for x in non_points]))))
        else:
            break

    return [int(x) for x in keep]


# Gets verified player decision
def verify_user_input():
    user_input = input("Please pick a number from the following options:\n1. Hold some dice and roll again.\n"
                       "2. End turn and keep points\n")
    while True:
        if user_input.isdigit():
            if 0 < int(user_input) < 3:
                return int(user_input)
        user_input = input("You didn't enter a valid option.\nPlease pick a number from the following options:\n"
                           "1. Hold some dice and roll again.\n"
                           "2. End turn and keep points\n")


# Main point calculating function
def point_count(set_aside, current_roll):

    points = 0

    available_dice = set_aside + [[int(x) for x in current_roll]]

    non_points = []

    for roll in available_dice:

        # Check for straights
        if {1, 2, 3, 4, 5, 6} == set(roll):
            points += 1000
            roll = [x for x in roll if str(x) not in '123456']
        if {1, 2, 3, 4, 5} == set(roll):
            points += 500
            [roll.remove(x+1) for x in range(5)]

        pair_count = 0

        for di in roll:

            # Calculate multiples
            if str(roll).count(str(di)) >= 3:
                multiple = 0
                if di == 1:
                    multiple += di*1000
                else:
                    multiple += di*100
                # Double value for each di after 3
                for x in range(roll.count(di)-3):
                    multiple *= 2
                points += multiple
                roll = [x for x in roll if x != di]  # Remove all of current di occurrences from the roll

            if roll.count(di) == 2:  # Count pairs in roll
                pair_count += 1

        if pair_count == 6:
            points += 500
            roll = []

        for di in roll[:]:
            for value in set_aside:  # Check current hand for previous multiples and remove them
                # print(value)
                if str(value).count(str(di)) >= 3:
                    points += 100
                    roll.remove(di)

        for di in roll:
            if di == 1:
                points += 100
            elif di == 5:
                points += 50
            else:
                non_points.append(di)

    return points, non_points
