#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import math 

def is_loadable(load, num_truck, w_list):

    excess = load*num_truck - sum(w_list)
    # print('Minimum Load:', load, num_truck, 'excess:', excess)
    cur_load = 0
    #truck_load = list()
    for w in w_list:
        #print(cur_load, w)
        if cur_load + w < load:
            cur_load += w
        elif cur_load + w == load:
            #truck_load.append(cur_load + w)
            cur_load = 0
            num_truck -= 1
            if num_truck < 0:
                return False
        else:
            num_truck -= 1
            if num_truck < 0:
                return False
            excess += load - cur_load
            if excess < 0:
                return False
            #print(cur_load, 'is added')
            #truck_load.append(cur_load)
            cur_load = w

    #truck_load.append(cur_load)
    if (cur_load and num_truck == 0):
        return False
    #print(truck_load)
    return True

n, num_truck = map(int, sys.stdin.readline().split())

weight = list()
for i in range(n):
    weight.append(int(sys.stdin.readline()))

ave_w = sum(weight) / num_truck
max_w = max(weight)
load = max(max_w, math.ceil(ave_w))
max_ng = load - 1

while True:
    if is_loadable(load, num_truck, weight):
        break
    min_ng = load
    load += 1024

min_ok = load
while True:
    if min_ok == max_ng + 1:
        break
    load = (max_ng + min_ok) // 2
    if is_loadable(load, num_truck, weight):
        min_ok = load
    else:
        max_ng = load

print(min_ok)
