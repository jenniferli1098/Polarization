from model import Model
import numpy as np
def __main__():
    example_1()


def example_1():
    model1 = Model(1)
    a_candidates = np.array([1,0,-1])
    
    p_candidates = np.array([0.01,0.99,0.01]) #worst case
    # p_candidates = np.array([0.99,0.99,0.01]) #agent-optimizing case
    model1.create_candidates(a_candidates, p_candidates)

    a_voters = np.array([-1,-1,-1,1,1])
    r_voters = np.array([[1,0.1,0],[1,0.1,0],[1,0.1,0],[0,1,0.1],[0,1,0.1]])
    model1.create_voters(a_voters, r_voters, a_candidates)

    states = np.arange(0,1.01,0.1)
    model1.create_states(states)
    model1.set_state(1)
    model1.set_voting_rule("plurality")
    model1.set_type("mallows")  #mallows or deterministic (default)

    model1.run_simulation(num_rounds = 1000)
    model1.history.stats()


__main__()