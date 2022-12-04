def is_prime(x):
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for m in range(5, int(x**0.5) + 1, 6):
        if x % m == 0 or x % (m + 2) == 0:
            return False
    return True


assert is_prime(-1) == False
assert is_prime(0) == False
assert is_prime(1) == False
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(5) == True

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
