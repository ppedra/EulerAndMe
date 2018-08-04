"""
Euler Project 2
https://projecteuler.net/problem=2
"""

#lets find the fibonnaci numbers and sum the even ones
def fibonnaci(limit):
    a0=1
    a1=2
    s=0
    while True:
        #end condition
        if a1>(limit):
            return s
        #if even, sum on s
        if a1%2==0:
            s=s+a1
        #do the magic
        a0,a1=a1,a0+a1

print(fibonnaci(4*(10**6)))

