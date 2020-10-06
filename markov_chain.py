from collections import defaultdict, deque
from random import choice, random
import pickle


class MarkovChain:
    """A word based markov chain. """

    def __init__(self, n: int):
        self.n = n
        self.counts = defaultdict(dict)
        self.initial_words = set()

    def process_file(self, file_name: str):
        """Add file to the transition probability mapping. """
        with open(file_name) as f:
            for line in f.readlines():
                lense = deque(maxlen=self.n)
                words = line.split()
                words = [x.lower() for x in words]
                for word, next_word in zip(words, words[1:]):
                    lense.append(word)
                    if len(lense) == self.n:
                        self.initial_words.add(word)
                        state = ' '.join(lense)
                        if next_word not in self.counts[state]:
                            self.counts[state][next_word] = 0
                        self.counts[state][next_word] += 1

    def save_counts(self, file_name='markov-counts'):
        with open(file_name, 'wb') as f:
            pickle.dump(self.counts, f)

    def load_counts(self, file_name='markov-counts'):
        with open(file_name, 'rb') as f:
            self.counts = pickle.load(f)
            # self.counts.update(pickle.load(f))

    def generate(self, k):
        """Take a walk of length k through the markov chain. """
        assert k > self.n

        def weighted_sample(counts):
            """
            This function takes a weighted sample from a counter
            counts maps words to an integer count.
            """
            population = sum(counts.values())
            threshold = 0
            roll = random()
            for word in counts:
                threshold += counts[word]
                if roll < threshold / population:
                    return word

        # import pdb
        # pdb.set_trace()

        # start = choice(tuple(self.initial_words))
        start = choice(tuple(self.counts))
        walk = start.split()  # list of strings
        for _ in range(k):
            # state needs to be a single string containing self.n words
            state = ' '.join(walk[-self.n:])
            walk.append(weighted_sample(self.counts[state]))
        return ' '.join(walk)
