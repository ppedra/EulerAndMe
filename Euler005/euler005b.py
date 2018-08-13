"""
Euler 005
"""
import timeit

def is_dividable_by_range(lim):
    """check first the primes and then the remaining"""

    #print("check which number is evenly divisible by",list(range(1,lim+1)))
    primes = [2,3,5,7,11,13]

    list_to_check = list(range(1,lim+1))
    for num in list_to_check:
        if num in primes:
            list_to_check.remove(num)

    num = 1
    while True:
        is_dividable = True
        #print("num:",num)

        for i in primes:
            if num%i!=0:
                is_dividable=False
                break    

        if is_dividable:
            for i in list_to_check:
                if num%i!=0:
                    is_dividable=False
                    break

        if is_dividable:
            print(num,"is evenly divisible by",list(range(1,lim+1)))
            #print("--")
            break
        
        num+=1

if __name__ == "__main__":
    print(timeit.timeit("is_dividable_by_range(20)",globals=globals(),number=1))

        