#!/usr/bin/env python3

def isprime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, n):
        if (n % i == 0):
            return False
    return True

num = 0
i = 0
# for i in range(2, 100):
while num < 10002:
    if isprime(i) == True:
        if num == 10001:
            print(i)
        # print("{:<5}{:<5}".format(num, i))
        num += 1
    i += 1
