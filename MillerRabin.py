# Implementation of the Miller-Rabin primality test.  

from random import randint
from modpower import modpower
from xgcd import gcd

def MillerRabinOnce(p,a):
    '''runs the Miller-Rabin primality test once'''
    assert p % 2 == 1 # p should be odd
    r = p-1
    u = 0
    #find number of times 2 divides p-1
    while r % 2 == 0:
        r = r//2
        u = u + 1
    y = modpower(a,r,p)
    if y == 1:
        return True
    for i in range(u):
        if y == p-1:
            return True
        y = (y*y) % p
    return False


def isPrime(p,k=20):
    '''repeats Miller-Rabin k times on p''' 
    for i in range(k):
        a = randint(1,p-1)
        if gcd(a,p) != 1:
            return False # then p can't be prime
        if not MillerRabinOnce(p,a):
            return False  
    return True


def findPrime(a,b,k=20):
    '''finds a random prime in the interval [a,b]'''
    PROD = 3*5*7*11*13*17*19*23*29*31*37*41*43*47 # product of small primes 
    p = randint(a,b)
    if p % 2 == 0:
        p = p+1 # p should be odd
    while not isPrime(p,k):
        p = p + 2  # try next case
        while gcd(p,PROD) != 1:  # check for divisibility by a small prime
            p = p + 2
    return p
