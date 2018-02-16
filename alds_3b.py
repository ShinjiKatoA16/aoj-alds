#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

n, quantum = map(int, sys.stdin.readline().split())

proc_q = list()
for i in range(n):
    p_name, length = sys.stdin.readline().split()
    proc_q.append([p_name, int(length)])

elapse = 0
while proc_q:
    process = proc_q.pop(0)  # retrieve 1st element
    p_time = min(quantum, process[1])
    elapse += p_time
    if p_time == process[1]:
        print(process[0], elapse)
    else:
        proc_q.append([process[0], process[1]-quantum])
