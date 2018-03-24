#!/usr/bin/env python3

data = []

with open("data.txt") as datafile:
    content = datafile.readlines()

    for line in content:
        a = line.strip("\n")
        data.append(a)

res = "".join(data)

biggest = 0

for z in range(0, 1000 - 13):
    a = int(res[z])
    b = int(res[z + 1])
    c = int(res[z + 2])
    d = int(res[z + 3])

    e = int(res[z + 4])
    f = int(res[z + 5])
    g = int(res[z + 6])
    h = int(res[z + 7])

    i = int(res[z + 8])
    j = int(res[z + 9])
    k = int(res[z + 10])
    l = int(res[z + 11])

    m = int(res[z + 12])

    result = a * b * c * d * e * f * g * h * i * j * k * l * m
    # print(result)
    if result > biggest:
        biggest = result

print(biggest)
