#!/usr/bin/env python3

def prime_fact(val):
    lista = []
    sux = 1
    largest = 0
    for i in range(1, val):
        if val % i == 0:
            sux = sux * i
            if sux == val:
                largest = i
                print(largest)
                break

prime_fact(600851475143)
