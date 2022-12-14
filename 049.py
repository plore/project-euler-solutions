from helpers import is_prime, primes_up_to


def are_permutations(a: int, b: int) -> bool:
    freqs_a = [0] * 10
    freqs_b = [0] * 10
    for c in str(a):
        freqs_a[int(c)] += 1
    for c in str(b):
        freqs_b[int(c)] += 1
    for x in range(10):
        if freqs_b[x] != freqs_a[x]:
            return False
    return True


assert are_permutations(1234, 4321)
assert are_permutations(1234, 1324)
assert are_permutations(1234, 1234)
assert are_permutations(1111, 1111)
assert not are_permutations(1111, 1112)
assert not are_permutations(1111, 111)

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
