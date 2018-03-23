#!/usr/bin/env python3

import time

start = time.time()

lista = []

list_range = 10000

for i in range(0, list_range):
    lista.append(0)

lista[1] = 1
lista[2] = 1

# print("{:<5}{:<5}{:<20}".format("n", "len", "val"))

biggest_nr = 0

n = 3
while n < list_range:
    lista[n] = lista[n-1] + lista[n-2]
    # print("{:<5}{:<5}{:<20}".format(n, len(str(lista[n])), str(lista[n])[:10]))
    if len(str(lista[n])) < 1000:
        biggest_nr = n
        n += 1
    else:
        break

print(str(lista[biggest_nr+1])[:10])
