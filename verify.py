def verify_players():
    return int(input("How many players? "))


def verify_roll(dice, set_aside, roll_count):
    if '1' in set(dice) or '5' in set(dice):
        return True
    possibilities = len(dice)
    for x in dice:
        if x not in "15": # Not a 1 or a 5
            if dice.count(x) < 3: # Less than 3
                # for value in set_aside.values(): # Check current hand
                #     if str(value).count(x) >= 3:
                #         return True
                possibilities -= 1
    if possibilities == 0:
        return False
    return True


def verify_keep(current_roll):
    # todo Add point value verification
    keep = input("Which would you like to hold? ")
    while True:
        if keep.isdigit():
            for i in keep:
                if keep.count(i) > current_roll.count(i):
                    keep = ''.join(input("Those weren't all in your roll.\n"
                                         "Please enter only numbers from your current roll of %s.\n"
                                         "Which would you like to hold? " % (' '.join(current_roll))))
        else:
            keep = ''.join(input("You entered non-numbers.\nPlease enter only numbers from your current roll of %s.\n"
                                 "Which would you like to hold? " % (' '.join(current_roll))))

        return [int(x) for x in keep]
