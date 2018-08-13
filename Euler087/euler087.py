import math

def find_primes(givenNumber):  
    
    # Initialize a list
    primes = []
    for possiblePrime in range(2, givenNumber + 1):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    
    return(primes)
    
#loop primes
lim = 50*(10**6)

primes = find_primes(int(math.sqrt(lim)+1))
#this math.sqrt(lim)+1 is a larger limit then we need but its ok here, it don't take that long to run

possible_num = []

for n1 in primes:
    n = n1**2
    if n > lim:
        #if only one component is larger then the limit:
        break

    for m1 in primes:
        m = m1**3
        if m > lim:
            break

        for o1 in primes:
            o = o1**4
            if o > lim:
                break
            
            num = n+m+o
            if (num < lim):
                possible_num.append(num)
            
print(len(set(possible_num)),"numbers smaller than",lim)