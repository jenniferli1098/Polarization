
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

    states = [0,1]
    model1.create_states(states)
    model1.set_state(0)
    for _ in range(10):
        model1.run_iter()
    print(model1.history.sum_utility())

__main__()