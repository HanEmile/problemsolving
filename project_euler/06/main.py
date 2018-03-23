#!/usr/bin/env python3

sum_a = 0

for i in range(1, 100 + 1):
    sum_a += i * i

a = 0
for i in range(1, 100 + 1):
    a += i

sum_b = a * a

print(sum_b - sum_a)
