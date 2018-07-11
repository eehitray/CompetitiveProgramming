def gen_primes(limit):
    '''sieve of eratosthenes'''
    #truth table for all primes
    a = [True] * limit   
    
    # 0 and 1 are not prime numbers
    a[0] = a[1] = False

    for i, isprime in enumerate(a):
        if isprime:
            # number at i is prime
            # add i to mem of gen
            yield i
            # mark all the multiples as not primes
            for n in range(i*i, limit, i):     
                a[n] = False

def is_prime(n):
    '''prime checker. nothing much'''
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
