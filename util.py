"""
An assortment of utility functions for the bot
"""
import pickle
from os.path import isfile
from os import system


class FallGuysWinCounter:
    def __init__(self):
        if isfile('win_counter'):
            with open('win_counter', 'rb') as f:
                self.wins = pickle.load(f)
        else:
            system('touch win_counter')
            self.wins = 0

    def _save_score(self):
        with open('win_counter', 'wb') as f:
            pickle.dump(self.wins, f)

    def increase(self):
        self.wins += 1
        self._save_score()

    def decrease(self):
        self.wins -= 1
        self._save_score()

    def get_wins(self):
        return self.wins


boy_win_counter = FallGuysWinCounter()
