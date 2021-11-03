import numpy as np
import random
phi = 1
def utility(a_candidate, a_voter, r, s):
    return (1 - s) * (a_candidate * a_voter + 1)/2 + s * r

def shuffle_dissimilarity(arr, d):
    temp = arr.copy()
    while True:
        random.shuffle(temp)
        if dissimarity_score(temp, arr) == d:
            return temp

def dissimarity_score(arr, temp):
    indices = zip(arr, range(len(arr)))
    indices = dict(indices)
    score = 0
    n = len(temp)
    for i in range(n):
        for k in range(i+1, n):
            if indices[i] > indices[k]:
                score += 1
    return score

#need to fix this
def cdf_mallows(n, percentile):
    # get normalizing denominator
    Z = 1
    term = 1
    c = 1
    for i in range(n-1):
        c *= phi
        term += c
        Z *= term

    d = 0
    sum = 1
    c = 1
    while sum / Z < percentile:
        d += 1
        c *= phi
        sum += c * 2
    return min(n,d) 

    