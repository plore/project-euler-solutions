from helpers import prime_factors

count = 0

for d in range(2, 12001):
    primes = prime_factors(d)
    n = int(1 / 3 * d) + 1
    while n / d < 1 / 2:
        coprime = not any(n % p == 0 for p in primes)
        count += 1 if coprime else 0
        n += 1

print(count)
