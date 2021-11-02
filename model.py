from util import utility
from candidate import Candidate
from voter import Voter
from statistics import mode
from random import shuffle
class Model:

    def __init__(self, id):
        self.id = id
        self.candidates = []
        self.voters = []
        self.states = []
        self.winners = []
        self.state = []
        self.round = 0

    def create_candidates(self, a, p):
        self.candidates = [Candidate(i,a[i], p[i]) for i in range(len(a))]

    def create_voters(self, a, r, a_c):
        self.voters = [Voter(i,a[i], r[i], a_c) for i in range(len(a))]

    def create_states(self, states):
        self.states = states
        self.cur_state = states[0]
    
    def find_winner(self, cur_state):
        rankings = [voter.determine_ranking(cur_state) for voter in self.voters]
        #for now, assume plurality
        scores = [rank[0] for rank in rankings]
        shuffle(scores)
        return mode(scores)

    def run_iter(self):
        id = self.find_winner(self.cur_state)
        print(id)
        self.round += 1
        self.winners.append(id)
        


