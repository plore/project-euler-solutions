from helpers import is_prime

# Since we start at n = 0, we can exclude:
# - all negative b since negative numbers are not prime
# - all positive b that are not primes themselves

viable_b = [b for b in range(1001) if is_prime(b)]

maxn = maxa = maxb = 0
for a in range(-1000, 1001):
    for b in viable_b:
        n = 0
        while is_prime(n**2 + a * n + b):
            n += 1
        if n > maxn:
            maxa = a
            maxb = b
            maxn = n

print(maxa * maxb)
