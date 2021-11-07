from model import Model
import numpy as np
import matplotlib.pyplot as plt
#testing when s is not as stable

  
def example_1(axis_x):
    model1 = Model(1)
    n = 100
    m = 7
    
    a_candidates = 2*np.random.rand(m)-1
    p_candidates = np.array([0]*m) #agent-optimizing case
    # a_voters = np.array([-1,-1,-1,1,1])
    a_voters = 2*np.random.rand(n)-1
    # print(a_voters)
    r_voters = np.random.rand(n,m)
    for i in range(len(r_voters)):
        row = r_voters[i]
        sum = np.sum(row)
        r_voters[i] = row/sum
    # print(r_voters)
    # r_voters = np.array([
    #     [1,0.1,0],
    #     [1,0.1,0],
    #     [1,0.1,0],
    #     [0,1,0.1],
    #     [0,1,0.1]]
    #     )
        
        
    model1.create_candidates(a_candidates, p_candidates)
    model1.create_voters(a_voters, r_voters, a_candidates)
    model1.set_type("deterministic")  #mallows or deterministic (default)

    x = np.arange(0,1,0.01)
    y_borda = []
    y_plural = []
    for i in x:
        states = np.array([i])
        model1.create_states(states)
        #set as borda 
        model1.set_voting_rule("borda")
        model1.run_simulation(num_rounds = 1)
        y_borda.append(model1.history.rounds[0].utility)
        
        #set as plurality
        model1.set_voting_rule("plurality")
        model1.run_simulation(num_rounds = 1)
        y_plural.append(model1.history.rounds[0].utility)
    # print(y)
    plt.subplot(5, 2,axis_x)
    plt.plot(x, y_borda,"-",label="Borda")
    plt.plot(x, y_plural,"-",label="Plurality") 



np.random.seed(1)
fig, axes = plt.subplots(5, 2) 
for i in range(10):
    example_1(i+1)
# fig.show()
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
plt.show()