#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def bsearch(val, _list):
    i_min = 0
    i_max = len(_list) - 1
    while True:
        i_mid = (i_min + i_max) // 2  # i_min + (i_max-i_min) // 2, if integer overflow can occur
        m_val = _list[i_mid]
        # print(val, m_val, i_mid, i_min, i_max)
        if val == m_val:
            return True
        elif val < m_val:
            i_max = i_mid - 1
            if i_max < i_min:
                return False
        else:
            i_min = i_mid + 1
            if i_min > i_max:
                return False

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))

total = 0

for x in t:
    if bsearch(x, s):
        total += 1

print(total)
