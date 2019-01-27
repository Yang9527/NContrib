# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 21:03:26 2019

@author: zyy
"""

import numpy as np
import cvxopt as opt

def load_data(filename):
    with open(filename) as fin:
        lines = fin.readlines()
        lines = [line.strip().split() for line in lines if line.strip() != ""]
        lines = [[float(x) for x in line] for line in lines]
        return lines

def solve(records):
    """
    
    """
    records = np.array(records) 
    X = records[:, 0:1]
    S = records[:, 1:]
    P = opt.matrix(np.dot(S.T, S))
    q = opt.matrix(-np.dot(S.T, X))
    A = opt.matrix([[1.0],[1],[1],[1],[1]])
    print(A)
    b = opt.matrix(np.array([1.0]))
    G = opt.matrix(np.diag([-1,-1.0,-1,-1,-1]))
    h = opt.matrix(np.zeros(5))
    sol = opt.solvers.qp(P,q,G,h,A,b)
    print(sol['x'])


if __name__ == "__main__":
    data = load_data("data.txt")
    solve(data[:2])
    
