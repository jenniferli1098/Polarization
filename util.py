import numpy as np
import random
import statistics

def utility(a_candidate, a_voter, r, s):
    return (1 - s) * (a_candidate * a_voter + 1)/2 + s * r


def borda(profile,m,n):
    points = {i:0 for i in np.arange(m)} #i+1 if you want to index from 1
    for v in range(n):
        curr_points = m-1
        for pos in profile[v]:
            points[pos] += curr_points
            curr_points -=1
    key, _ = max(points.items(),key = lambda i : i[1])
    return key

def plurality(profile,m,n):
    scores = [rank[0] for rank in profile]
    random.shuffle(scores)
    return statistics.mode(scores)

    
def sampleFromMallows(ranking, phi):
    # print(ranking)
    m = np.size(ranking)
    z = np.zeros(m)
    z[0] = ranking[0]
    for i in range(1,m):
        #print("i = ", i)
        temp = z.copy()
        r = np.random.random_sample()
        flag = 0
        d = 0
        for k in range(0,i+1):
            d += phi**k
        c = 0.0
        #insert ranking[i] into z[j] with probability p_j / d
        for j in range(0,i+1):
            #print(" j = ", j)
            p = (phi**(i-j)) / d
            c += p
            #print(" c = ", c)

            if flag:
                temp[j] = z[j-1]
            else:
                if r <= c:
                    flag = 1
                    temp[j] = ranking[i]
                    #print("insert ", ranking[i], " at ", j)
                else:
                    temp[j] = z[j]
        z = temp
    #print("noisy ranking = ", z)
    return [int(i) for i in z]
