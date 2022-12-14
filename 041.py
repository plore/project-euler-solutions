from itertools import permutations

from helpers import is_prime, to_num

for n in range(9, 3, -1):
    p = permutations(range(1, n + 1))
    primes = [to_num(perm) for perm in p if is_prime(to_num(perm))]
    if len(primes) > 0:
        print(max(primes))
        break
