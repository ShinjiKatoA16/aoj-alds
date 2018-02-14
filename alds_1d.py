#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())
r = list()
for i in range(n):
    r.append(int(sys.stdin.readline()))

max_diff = min(r) - max(r)
max_v = r[0]

for i in range(n-1):
    if r[i] == max_v:
        max_v = max(r[i+1:])
    diff = max_v - r[i]
    if diff > max_diff:
        max_diff = diff

print(max_diff)

