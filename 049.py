from helpers import are_permutations, is_prime, primes_up_to

primes = [p for p in primes_up_to(10000) if p > 1000]

for idx, p in enumerate(primes):
    if p in (1487, 4817, 8147):
        continue
    for q in primes[idx + 1 :]:
        if not are_permutations(p, q):
            continue
        r = q + (q - p)
        if is_prime(r) and are_permutations(r, q):
            print(str(p) + str(q) + str(r))
            break
