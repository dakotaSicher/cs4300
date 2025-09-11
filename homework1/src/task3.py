def sign(arg1):
    try:
        if(arg1 > 0):
            return "positive"
        elif(arg1 < 0):
            return "negative"
        else:
            return "zero"
    except TypeError:
        raise

def primesList(n=10):
    n -= 1
    primes = [2]
    next = 3
    while n > 0:
        for p in primes:
            if next % p == 0:
                break
        else:
            primes.append(next)
            n -= 1
        next += 2
    return primes

def sumN(n=100):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum