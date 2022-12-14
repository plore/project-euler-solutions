from helpers import is_prime, primes_up_to

# The sequence will be longer than 20 primes, so to stay below the one million total,
# regard only primes smaller than 1000000 / 20
primes = primes_up_to(50000)

maxlen = 0
maxprime = 0
for i, p_start in enumerate(primes):
    series_total = p_start
    k = 1
    while series_total < 1000000 and i + k + 1 < len(primes):
        if k > maxlen and is_prime(series_total):
            maxlen = k
            maxprime = series_total
        # Add next two primes to avoid even numbers
        series_total += primes[i + k] + primes[i + k + 1]
        k += 2

print(maxprime)
