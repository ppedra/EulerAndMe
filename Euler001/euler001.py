"""
Euler Project 1
https://projecteuler.net/problem=1
"""
l = []

limit=1000

for base_multiple in [3,5]:
    for i in range(limit):
        product = i*base_multiple
        if product>=limit: 
            break
        l.append(product)

print(sum(set(l)))
