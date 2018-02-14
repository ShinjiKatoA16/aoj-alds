#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def prt_list(A):
    s_list = list(map(str, A))
    print(' '.join(s_list))


def insert_sort(A):
    prt_list(A)
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        prt_list(A)
    return

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

insert_sort(a)
