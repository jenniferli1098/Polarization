class Candidate:
    def __init__(self, id, affiliation, p):
        self.id = id
        self.affiliation = affiliation
        self.p = p
        self.utility = 0

    def stats(self):
        print("Candidate ID: ",self.id)
        print("Affiliation: ",self.affiliation)
        print("Probability: ",self.p)