from typeguard import typechecked

@typechecked
def sign(arg1:int|float)->str:
    """
    Gets the sign of the value

    Args:
        arg1(int or float): The number

    Returns:
        A string description of the sign or 'zero'
    """
    if(arg1 > 0):
        return "positive"
    elif(arg1 < 0):
        return "negative"
    else:
        return "zero"


@typechecked
def primesList(n:int=10)->list[int]:
    """
    Args:
        n: number of primes to find

    Returns: The first n primes
    """
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

@typechecked
def sumN(n:int=100)->int:
    """
    Calculates the sum of integers from 1 to n
    """
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

if __name__ == "__main__":
    num = input("enter a number: ")
    print(sign(float(num)))

    num = input("How many primes you want?: ")
    print(primesList(int(num)))

    num = input("enter number to sum: ")
    print(sumN(int(num)))
    