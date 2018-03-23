#!/usr/bin/env python3

val = 1
big_val = 0
while val < 232792561:

    for i in range(1, 20):
        if ((val % i) == 0):
            if i == 18:
                # print(f"{val} / {i} == 0")
                big_val = val
        else:
            break

    val += 1

print(big_val)
