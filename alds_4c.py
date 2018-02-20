#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

_dict = dict()

n = int(sys.stdin.readline())
for i in range(n):
    cmd, word = sys.stdin.readline().split()
    if cmd == 'insert':
        _dict[word] = True
    elif cmd == 'find':
        if word in _dict:
            print('yes')
        else:
            print('no')
