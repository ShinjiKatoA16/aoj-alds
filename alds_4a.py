#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())
t = list(map(int, sys.stdin.readline().split()))

s_set = set(s)
total = 0

for x in t:
    if x in s_set:
        total += 1

print(total)
