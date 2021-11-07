from candidate import Candidate
from history import History
from voter import Voter
from util import borda, plurality
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
        self.voting_rule = "plurality"
        self.type = "deterministic"

    def create_candidates(self, a, p):
        self.candidates = [Candidate(i,a[i], p[i]) for i in range(len(a))]

    def create_voters(self, a, r, a_c):
        self.voters = np.array([Voter(i,a[i], r[i], a_c) for i in range(len(a))])
        R = np.array(r).T
        # print(R)
        for i in range(len(self.candidates)):
            self.candidates[i].utility = np.sum(R[i])

    def create_states(self, states):
        self.states = states
        self.history = History(len(states))

    def set_state(self, state):
        vals = np.where(self.states == state)
        self.cur_state_ind = vals[0][0] if len(vals[0]) > 0 else 0

    def set_type(self, type):
        self.type = type
        for voter in self.voters:
            voter.set_type(type)

    def set_voting_rule(self, vr):
        self.voting_rule = vr
    
    def find_winner(self, cur_state):
        profiles = [voter.determine_ranking(cur_state) for voter in self.voters]
        #for now, assume plurality
        if self.voting_rule == "plurality":
            return plurality(profiles, len(self.candidates), len(self.voters))
        elif self.voting_rule == "borda":
            return borda(profiles, len(self.candidates), len(self.voters))


    
    def run_simulation(self, num_rounds):
        #refresh
        self.history = History(len(self.states))
        for _ in range(num_rounds):
            self.run_iter()

    def run_iter(self):
        #find winner of the round
        state = self.states[self.cur_state_ind]
        winner_id = self.find_winner(state)
        winner = self.candidates[winner_id]
        # print("winner",winner_id)
        
        #increment round and add to history
        # print(winner.id, state, winner.utility)
        self.history.add_to_history(winner.id, state, winner.utility)

        #determine next state
        p = winner.p
        if random.uniform(0,1) < p:
            #move to the right
            self.cur_state_ind = min(self.cur_state_ind+1, len(self.states)-1)
        else:
            #move to the left
            self.cur_state_ind = max(self.cur_state_ind-1,0)
        


