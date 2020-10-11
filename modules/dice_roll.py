import re
from asyncio import create_task
from random import choice

import discord

from .base import Base


class DiceRoller(Base):
    def __init__(self):
        self._regex = r'^(\d*)d(\d+)([\+-]\d+)?$'

    def _is_valid_message(self, message: str) -> bool:
        """
        Predicate function.
        True indicates that this class can operate on the message
        False indicates that this class can not operate on the message
        """
        if match := re.match(self._regex, message):
            self._match = match
            self._number_of_dice = match.group(1)
            self._order = int(match.group(2))
            self._modifier = match.group(3)
            return True
        return False

    def _dice_roll(self):
        """Roll a dice of order self._order. """
        return choice(range(1, self._order + 1))

    async def __call__(self, message: discord.Message) -> None:
        # if the message is not valid return None
        if not self._is_valid_message(message.content):
            return
        # else compute a response and send a message
        rolls = ''
        total = 0
        if self._number_of_dice:
            self._number_of_dice = int(self._number_of_dice)
            for i in range(self._number_of_dice):
                roll = self._dice_roll()
                rolls += f'{roll}{"+" if i < self._number_of_dice - 1 else ""}'
                total += roll
        else:
            # only roll one dice
            roll = self._dice_roll()
            total = roll
            rolls = f'{roll}'
        if self._modifier:
            # add the modifier
            self._modifier = int(self._modifier)
            if self._modifier > 0:
                create_task(message.channel.send(
                    f'[{rolls}]+{self._modifier}={total + self._modifier}'))
            else:
                create_task(message.channel.send(
                    f'[{rolls}]-{-self._modifier}={total + self._modifier}'))
        else:
            create_task(message.channel.send(f'[{rolls}]={total}'))
