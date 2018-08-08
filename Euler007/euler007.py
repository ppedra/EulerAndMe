def find_primes(lim = 100):
    """ 
    if is divisible by smaller primes, is not prime (of course) 
    if is divisible by, let's say 8, this is also verified on the division by 2, witch is prime
    """
    #some know primes (without 1)
    primes = [2,3,5]

    for num in range(primes[-1], lim):
        #innocent/prime until proven otherwise
        is_prime = True

        for prime in primes:
            if (num%prime==0):
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)

    #add 1 in position 0 to return all primes
    primes.insert(0,1)

    return primes


if __name__ == "__main__":

    index = 10001       
    l = find_primes(10**9)

    if len(l)>=index:
        print(l[index])
    else:
        print("lim too small")

