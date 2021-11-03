
from statistics import mode
from model import Model


def __main__():
    example_1()


def example_1():
    model1 = Model(1)
    a_candidates = [1,0,-1]
    p_candidates = [0.01,0.99,0.01]
    model1.create_candidates(a_candidates, p_candidates)

    a_voters = [-1,-1,-1,1,1]
    r_voters = [[1,0.1,0],[1,0.1,0],[1,0.1,0],[0,1,0.1],[0,1,0.1]]
    model1.create_voters(a_voters, r_voters, a_candidates)

    states = [0,0.25,0.5,0.75,1]
    model1.create_states(states)
    model1.set_state(1)
    model1.set_voting_rule("plurality")

    for _ in range(1000):
        model1.run_iter()
    model1.history.stats()

__main__()