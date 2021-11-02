from candidate import Candidate
from history import History
from voter import Voter
import statistics
import random
import numpy as np
class Model:

    def __init__(self, id):
        self.id = id
        self.candidates = []
        self.voters = []
        self.states = []
        self.cur_state_ind = 0
        self.round = 0
        self.history = History()

    def create_candidates(self, a, p):
        self.candidates = [Candidate(i,a[i], p[i]) for i in range(len(a))]

    def create_voters(self, a, r, a_c):
        self.voters = [Voter(i,a[i], r[i], a_c) for i in range(len(a))]
        R = np.array(r).T
        print(R)
        for i in range(len(self.candidates)):
            self.candidates[i].utility = np.sum(R[i])
    def create_states(self, states):
        self.states = states

    def set_state(self, state):
        self.cur_state_ind = max(self.states.index(state),0)
    
    def find_winner(self, cur_state):
        rankings = [voter.determine_ranking(cur_state) for voter in self.voters]
        #for now, assume plurality
        scores = [rank[0] for rank in rankings]
        random.shuffle(scores)
        return statistics.mode(scores)

    def run_iter(self):
        #find winner of the round
        state = self.states[self.cur_state_ind]
        winner_id = self.find_winner(state)
        winner = self.candidates[winner_id]
        print("winner",winner_id)
        
        #increment round and add to history
        print(winner.id, state, winner.utility)
        self.history.add_to_history(winner.id, state, winner.utility)

        #determine next state
        p = winner.p
        if random.uniform(0,1) < p:
            #move to the right
            self.cur_state_ind = min(self.cur_state_ind+1, len(self.states))
        else:
            #move to the left
            self.cur_state_ind = max(self.cur_state_ind-1,0)
        


