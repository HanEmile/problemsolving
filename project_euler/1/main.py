#!/usr/bin/env python3

sum_all = 0
a = 0

while a < 1000:
    if ((a % 3) == 0) or ((a % 5) == 0):
        sum_all += a

    a += 1

print(sum_all)
