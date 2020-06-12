# file that defines the player class
# players exist within the dnd channel such that various useful statistics can be tracked
# dice roll history being one of these
from random import choice


def dice_roll(x: int):
    return choice(range(1, x + 1))


class Player():

    """This class exists to facilitate dice rolling statistics"""

    def __init__(self, num: int):
        """TODO: to be defined. """
        self.num = num
        self.dice_roll_history = dict()

    def dice_roll(self, x: int) -> int:
        # this function takes in a dice number and returns a roll of that dice and records the dice roll
        roll = choice(range(1, x + 1))
        if roll in self.dice_roll_history:
            self.dice_roll_history[x].append(roll)
        else:
            self.dice_roll_history[x] = [roll]
        return roll
