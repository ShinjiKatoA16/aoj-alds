#!/usr/bin/python3
# -*- coding: utf-8 -*-

def solve(p, t, A, result):
    if A[p] == t:
        result[(p,t)] = True
        return True
    if p == len(A) - 1:
        return False
    if (p,t) in result:
        # print('Cache Hit')
        return result[(p,t)]
    if solve(p+1, t-A[p], A, result):
        result[(p,t)] = True
        return True
    if solve(p+1, t, A, result):
        result[(p,t)] = True
        return True
    result[(p,t)] = False 
    return False

import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
num_q = int(sys.stdin.readline())
query = list(map(int, sys.stdin.readline().split()))
result = dict()

for m in query:
    if solve(0, m, A, result):
        print('yes')
    else:
        print('no')
