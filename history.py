from util import utility
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

    def sum_utility(self):
        utility = [round.utility for round in self.rounds]
        return sum(utility)

