from helpers import primes_up_to

# For each denominator d, Euler's Totient function gives the number of irreducible fractions n / d.

primes = primes_up_to(1000000)

totients = [1] * 1000001

for p in primes:
    totients[p] = p - 1

for d in range(2, 1000000 + 1):
    if totients[d] > 1:
        continue

    p = next(prime for prime in primes if d % prime == 0)

    x = d
    m = 0
    while x % p == 0:
        x //= p
        m += 1
    totients[d] *= p ** (m - 1) * (p - 1)

    # since d / x contains all the occurrences of p in d, no common prime factor remains between x and d / x.
    # Therefore gcd(d, d/x) = 1 and we can use the multiplicative property of the Totient function.
    totients[d] *= totients[int(x)]

print(sum(totients[2:]))
