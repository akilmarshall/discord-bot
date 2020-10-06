import markov_chain
from random import choice

MC = markov_chain.MarkovChain(4)
MC.load_counts()
PRIMES = [5, 7, 11, 13, 17]


def pol_bot():
    return MC.generate(choice(PRIMES))
