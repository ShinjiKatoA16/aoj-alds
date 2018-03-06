#!/usr/bin/python3
# -*- coding: utf-8 -*-

def Merge(A, left, mid, right):
    L = A[left:mid]
    R = A[mid:right]
    L.append(None)
    R.append(None)
    item_L = L.pop(0)
    item_R = R.pop(0)

    global cmp_count
    for i in range(left, right):
        cmp_count += 1
        if item_L == None:
            A[i] = item_R
            item_R = R.pop(0)
        elif item_R == None:
            A[i] = item_L
            item_L = L.pop(0)
        elif item_L <= item_R:
            A[i] = item_L
            item_L = L.pop(0)
        else:
            A[i] = item_R
            item_R = R.pop(0)

def Merge_Sort(A, left, right):
    if left+1 < right:
        mid = (left + right) // 2
        Merge_Sort(A, left, mid)
        Merge_Sort(A, mid, right)
        Merge(A, left, mid, right)


import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

cmp_count = 0
Merge_Sort(A, 0, len(A))
print(' '.join(map(str,A)))
print(cmp_count)
