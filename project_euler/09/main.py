#!/usr/bin/env python3

solution = False

for a in range(1, 1000):
    if solution == True:
        break

    for b in range(1, 1000):
        for c in range(1, 1000):
            if a * a + b * b == c * c:
                if a + b + c == 1000:
                    print(a * b * c)
                    solution = True
