from .base import Base
from .markov_chain import MarkovChain
from random import choice
from asyncio import create_task
import discord


class LanguageModel(Base):
    def __init__(self):
        self.MC = MarkovChain(4)
        self.MC.load_counts()
        self._PRIMES = [5, 7, 11, 13, 17, 23]

    def _is_valid_message(self, message: str) -> bool:
        if message in ['garbage', 'shit post', 'wwps', 'what would pol say?']:
            return True
        return False

    async def __call__(self, message: discord.Message) -> None:
        if not self._is_valid_message(message.content):
            return
        msg = self.MC.generate(choice(self._PRIMES))
        create_task(message.channel.send(msg))
