#!/usr/bin/env python3

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

sum_all = 0

n = 0
while F(n) < 4000000:
    a = F(n)
    if ((a % 2) == 0):
        sum_all += a
    n += 1

print(sum_all)
