#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

MAX_PRIME = 10**4
def prime_list():
    sqrt_max = int(MAX_PRIME ** 0.5)
    primes = [True for i in range(MAX_PRIME+1)]
    primes[0] = primes[1] = False

    for p in range(sqrt_max):
        if primes[p]:
            for px in range(p*2, MAX_PRIME, p):
                primes[px] = False

    p_list = [i for i in range(MAX_PRIME) if primes[i]]
    return p_list


def is_prime(n, prime_list):
    sqrt_n = int(n ** 0.5)
    for i in prime_list:
        if i > sqrt_n:
            break
        if n % i == 0:
            return False
    return True

p_list = prime_list()

n = int(sys.stdin.readline())
num_p = 0

for i in range(n):
    x = int(sys.stdin.readline())
    if is_prime(x, p_list):
        num_p += 1
print(num_p)
