#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

_list = list()

n = int(sys.stdin.readline())
for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'insert':
        # _list.insert(0, cmd[1])
        _list.append(cmd[1])
    elif cmd[0] == 'delete':
        try:
            tmp = _list[::-1]
            tmp.remove(cmd[1])
            _list = tmp[::-1]
        except ValueError:
            #print('skip deleting', cmd[1])
            pass
    elif cmd[0] == 'deleteFirst':
        _list.pop()
    elif cmd[0] == 'deleteLast':
        _list.pop(0)
    else:
        raise ValueError
    # print(_list)

print(' '.join(_list[::-1]))

