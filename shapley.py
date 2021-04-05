# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:20:57 2021

@author: Ahmad Al Musawi
"""
from itertools import permutations
import pandas as pd
import numpy as np



def start():
    V = [([1],100), ([2],125), ([3],50), ([1,2],270), ([1,3],375), ([2,3],350), ([1,2,3],500)]
    S = [Shapley(V, i) for i in permutations((1,2,3))]
    newS = []
    for i in S:
        a = []
        for j in i:
            a.append(j[1])
        newS.append(a)

    return expected_marginal(np.array(newS))
    
    
    
def expected_marginal(S):
    print(S)
    r, c = S.shape
    k = [sum(S[:, i])/r for i in range(c)]
    return k

    


def Shapley(V, C):
    """
    V: v values of Z and coalitions
    C: coalition to measure contribution of its zones based on order of arrival"""
    # print("V=", V)
    # print("C=", C)

    contribution = [get_v([C[0]], V)]
    coalition = [C[0]]
    for i in range(1, len(C)):
        new_coalition = coalition.copy()
        new_coalition.append(C[i])
        
        old_contr= get_v(coalition, V)
        new_contr= get_v(new_coalition, V)
        
        contribution.append(new_contr - old_contr )
        coalition = new_coalition.copy()
    
    return sort_tuples([(C[i], contribution[i]) for i in range(0, len(C))])
        
                    

def get_v(i, V):
    for v in V:
        if set(i) == set(v[0]):
            # print("v({}) = {}".format(i, v[1]))
            return v[1]
        

def sort_tuples(A):
    return sorted(A, key=lambda x: x[0])




