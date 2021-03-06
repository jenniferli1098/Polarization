from model import Model
import numpy as np
import matplotlib.pyplot as plt
#testing when s is not as stable

  
def example_1(axis_x):
    model1 = Model(1)
    n = 100
    m = 7
    
    a_candidates = np.random.default_rng().uniform(-1,1,m)
    p_candidates = np.array([0]*m) #agent-optimizing case
    # a_voters = np.array([-1,-1,-1,1,1])
    a_voters = np.random.default_rng().uniform(-1,1,n)
    # print(a_voters)
    r_voters = np.random.default_rng().uniform(-1,1,(n,m))
    # for i in range(len(r_voters)):
    #     row = r_voters[i]
    #     sum = np.sum(row)
        # r_voters[i] = row/sum
    # print(r_voters)
    # print(np.max(r_voters), np.min(r_voters))
    if axis_x == 10:
        print("round: ",axis_x)
        print("a_candidates",a_candidates.tolist())
        print("a_voters",a_voters.tolist())
        print("rvoters",r_voters.tolist())
        print([2,3,42,3])



        
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
    
    y_borda = np.array(y_borda)
    y_plural = np.array(y_plural)
    max_reward = 1# np.array([max([model1.actual_rewards(w, s) for w in range(m)])for s in x])
    # print(max_reward)

    # print(y)
    # plt.subplot(5, 2,axis_x)
    plt.plot(x, y_borda/max_reward,"-",label="Borda")
    plt.plot(x, y_plural/max_reward,"-",label="Plurality") 



# np.random.seed(0)
while True:
    # fig, axes = plt.subplots(5, 2) 
    # for i in range(10):
    example_1(10)
    # fig.show()
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
    plt.show()