from util import utility
class Voter:
    def __init__(self, id, affiliation, real_utility, candidate_affiliation):
        self.id = id
        self.affiliation = affiliation
        self.real_utility = real_utility
        self.candidate_affiliation = candidate_affiliation

    def compute_utility_candidate(self, state, candidate_id):
        return utility(self.candidate_affiliation[candidate_id], self.affiliation, self.real_utility[candidate_id], state)

    def determine_ranking(self, state):
        ids = list(range(len(self.real_utility)))
        ranking = sorted(ids, key=lambda id: -1* self.compute_utility_candidate(state, id))
        return ranking

    def stats(self):
        print("Voter ID: ",self.id)
        print("Affiliation: ",self.affiliation)
        print("Real Utility: ",self.real_utility)

