"""
Euler 005
"""
import timeit

def is_dividable_by_range(lim):
    print("check which number is evenly divisible by",list(range(1,lim+1)))

    #dumb way
    num = 1
    while True:
        is_dividable = True

        for i in range(1,lim+1):
            if num%i!=0:
                is_dividable=False
                break

        if is_dividable:
            print(num,"is evenly divisible by",list(range(1,lim+1)))
            print("--")
            break
        
        num+=1

if __name__ == "__main__":
    print(timeit.timeit("is_dividable_by_range(20)",globals=globals(),number=1))

        