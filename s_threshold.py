
from model import Model

import numpy as np
#testing when s is not as stable

  
def example_1():
    model1 = Model(1)
    a_candidates = np.array([1,0,-1])
    
    # p_candidates = np.array([0.01,0.99,0.01]) #worst case
    p_candidates = np.array([0.99,0.99,0.01]) #agent-optimizing case
    model1.create_candidates(a_candidates, p_candidates)

    a_voters = np.array([-1,-1,-1,1,1])
    r_voters = np.array([
        [1,0.1,0],
        [1,0.1,0],
        [1,0.1,0],
        [0,1,0.1],
        [0,1,0.1]]
        )
    model1.create_voters(a_voters, r_voters, a_candidates)

    # states = np.arange(0,1.01,0.1)
    states = np.array([1])
    model1.create_states(states)
    model1.set_state(1)
    model1.set_voting_rule("borda") #borda or plurality (default)
    model1.set_type("deterministic")  #mallows or deterministic (default)

    print(model1.candidates)
    model1.run_simulation(num_rounds = 1000)
    model1.history.stats()

example_1()