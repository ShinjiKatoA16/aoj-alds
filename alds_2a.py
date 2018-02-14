#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def bubble_sort(A):
    swap_count = 0
    for i in range(len(A)):
        for x in range(len(A)-1, i, -1):
            if A[x] < A[x-1]:
                swap_count += 1
                A[x], A[x-1] = A[x-1], A[x]

    return swap_count

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

swap_count = bubble_sort(A)
s_list = list(map(str, A))
print(' '.join(s_list))
print(swap_count)
