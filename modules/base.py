"""
Abstract class that all of the bot's modules inherit from
"""
import discord


class Base:
    def __init__(self):
        pass

    def _is_valid_message(self, message: str) -> bool:
        """
        Predicate function.
        True indicates that this class can operate on the message
        False indicates that this class can not operate on the message
        """
        pass

    async def __call__(self, message: discord.Message) -> None:
        pass
