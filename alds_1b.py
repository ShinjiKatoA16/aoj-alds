#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

x, y = map(int, sys.stdin.readline().split())
print(gcd(x, y))
