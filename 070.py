from helpers import are_permutations, primes_up_to

# From problem 69, to minimise n / phi(n), minimise the number of distinct prime factors of n and maximize the prime factors themselves.
# For a single prime p, n / phi(n) = p / (p - 1).
# Since p and p - 1 can never be permutations of each other, however, at least two prime factors p1 and p2 have to be used.

# Bold claim that the minimal ratio is smaller than 1.001 - if prime factor p1 exceeds 10000, p2 has to stay below 1000, yielding p2 / (p2 - 1) > 1.001
primes = primes_up_to(10000)

min_ratio = 2.0
min_n = 0
for idx, p1 in enumerate(primes[::-1]):
    for p2 in primes[idx:0:-1]:
        test = p1 * p2
        if test > 10000000:
            continue

        totient = p1 * (p2 - 1) if p1 == p2 else (p1 - 1) * (p2 - 1)

        if test / totient < min_ratio and are_permutations(test, totient):
            min_ratio = test / totient
            min_n = test

print(min_n)
