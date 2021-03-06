"""
Euler Library
=============

Support library for solving ProjectEuler problems
"""

# ==============================================================================

def numToList(x):
    """Convert an integer to list in reversed order"""

    if x == 0: return [0]

    lst = []
    while x > 0:
        lst.append(x % 10)
        x //= 10

    return lst
# ==============================================================================

def addList(u, v):
    """Add 2 number as lists in reversed representation"""

    ans = []
    i = j = c = 0
    while i < len(u) or j < len(v):
        s = c
        if i < len(u): 
            s += u[i]
            i += 1
        if j < len(v): 
            s += v[j]
            j += 1

        ans.append(s % 10)
        c = s // 10
    if c > 0:
        ans.append(c)
    return ans
# ==============================================================================

def totient(x):
    """Euler Totient function"""

    ans = x
    i = 2
    while i*i <= x:
        if x % i == 0:
            ans -= ans // i
            while x % i == 0:
                x //= i
        i += 1
    if x > 1:
        ans -= ans // x
    return ans
# ==============================================================================


def generatePrimes(N):
    """Generate prime numbers using Eratosthenes sieve"""

    half = N // 2 + 1
    sieve = [True] * half
    sieve[0] = False
    i = 1
    while 2*i*i < half:
        if sieve[i]: 
            curr = 3*i + 1
            while curr < half:
                sieve[curr] = False
                curr += 2*i + 1
        i += 1

    primes = [2]
    for i in range(3, N+1, 2):
        if sieve[i >> 1]:
            primes.append(i)
    return primes
# ==============================================================================


if __name__ == '__main__':
    for i in range(2, 10):
        print(totient(i))
