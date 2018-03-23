#!/usr/bin/env python3

def is_palin(val):
    str_a = str(val)
    str_b = str(val)[::-1]

    if str_a == str_b:
        return str_a
    else:
        return 0

biggest_palindrome = 0

for i in range(0, 999):
    for j in range(0, 999):
        k = 999 - i
        l = 999 - j

        if is_palin(k * j) != 0:
            if (k * j) > biggest_palindrome:
                biggest_palindrome = k * j

print(biggest_palindrome)
