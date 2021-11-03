from util import utility, shuffle_dissimilarity, cdf_mallows
import numpy as np
import random
class Voter:
    def __init__(self, id, affiliation, real_utility, candidate_affiliation):
        self.id = id
        self.affiliation = affiliation
        self.real_utility = real_utility
        self.candidate_affiliation = candidate_affiliation
        self.type = "deterministic"

    def determine_ranking(self, state):
        ids = np.arange(len(self.real_utility))
        util = utility(self.candidate_affiliation, self.affiliation, self.real_utility, state)
        ranking = sorted(ids, key=lambda id: -1* util[id])
        #now we shuffle
        if type == "mallows":
            d = cdf_mallows(len(self.real_utility), random.uniform(0,1))
            ranking = shuffle_dissimilarity(ranking, d)
        return ranking
    
    def set_type(self, type):
        self.type = type

    def stats(self):
        print("Voter ID: ",self.id)
        print("Affiliation: ",self.affiliation)
        print("Real Utility: ",self.real_utility)

