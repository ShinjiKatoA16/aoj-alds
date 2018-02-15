#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def insertSort(A, n, g):
    count = 0
    for i in range(g, n):
        v = A[i]
        x = i - g
        while x >= 0 and A[x] > v:
            A[x+g] = A[x]
            x = x - g
            count += 1
        A[x+g] = v
    return count

def shellSort(A, n):
    # 3h+1(... 121, 40, 13, 4, 1) is a good value for G[]
    G = list()
    h = 1
    count = 0
    while h <= n:
        G.append(h)
        h = h*3 + 1
    G = G[::-1] # Reverse
    m = len(G)
    for g in G:
        count += insertSort(A, n, g)

    print(m)
    print(' '.join(map(str, G)))
    print(count)
    for a in A:
        print(a)

n = int(sys.stdin.readline())
A = list()
for i in range(n):
    A.append(int(sys.stdin.readline()))

shellSort(A, n)
