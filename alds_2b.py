#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def selection_sort(A):
    swap_count = 0
    for i in range(len(A)):
        mini = i
        min_val = min(A[i:])
        min_index = A[i:].index(min_val) + i

        if A[min_index] < A[i]:
            swap_count += 1
            A[min_index], A[i] = A[i], A[min_index]

    return swap_count


n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

swap_count = selection_sort(A)
s_list = list(map(str, A))
print(' '.join(s_list))
print(swap_count)
