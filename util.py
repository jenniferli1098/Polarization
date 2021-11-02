def utility(a_candidate, a_voter, r, s):
    return (1 - s) * (a_candidate * a_voter + 1)/2 + s * r
