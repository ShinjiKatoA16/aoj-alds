#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def calc(operator, stack):
    val_b = stack.pop()
    val_a = stack.pop()

    if operator == '+':
        stack.append(val_a + val_b)
    elif operator == '-':
        stack.append(val_a - val_b)
    elif operator == '*':
        stack.append(val_a * val_b)
    else:
        raise ValueError

stack = list()
inline = sys.stdin.readline().split()  # List of string
for val in inline:
    if val in '+-*':
        calc(val, stack)
    else:
        stack.append(int(val))

print(stack.pop())

