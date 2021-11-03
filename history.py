from util import utility
import numpy as np
import collections
from matplotlib import pyplot as plt

class Round:
    def __init__(self, winner, state, utility):
        self.winner = winner
        self.state = state
        self.utility = utility

class History:
    def __init__(self):
        self.rounds = []

    def add_to_history(self, winner, state, utility):
        round = Round(winner, state, utility)
        self.rounds.append(round)
    
    def prev_round(self):
        if len(self.rounds) > 0:
            return self.rounds[len(self.rounds) - 1]
        else:
            return None

    
    # def state_freq(self):
    #     states = [round.state for round in self.rounds]
    #     return states
        # frequency = collections.Counter(utility)
        # return dict(frequency)


    def stats(self):
        
        utility = [round.utility for round in self.rounds]
        states = [round.state for round in self.rounds]
        print("total utility:      ", sum(utility))
        # print("frequency @ states: ", self.state_freq())
        hist, bin_edges = np.histogram(states, density=True)
        _ = plt.hist(hist, bins=bin_edges)  # arguments are passed to np.histogram
        plt.title("Histogram with 'auto' bins")
        plt.show()


