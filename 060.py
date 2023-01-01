from itertools import combinations

from helpers import is_prime, primes_up_to

primes = primes_up_to(10000)


def compatible(a: int, b: int) -> bool:
    sa = str(a)
    sb = str(b)
    return is_prime(int(sa + sb)) and is_prime(int(sb + sa))


assert compatible(3, 7)
assert compatible(3, 109)
assert compatible(3, 673)
assert compatible(7, 109)
assert compatible(7, 673)
assert compatible(109, 673)
assert not compatible(3, 5)

# Divide problem in half: primes p with p % 3 == 1 will only be compatible with other
# primes q with q % 3 == 1 as otherwise the concatenated number would be divisible by
# three.
# Same goes for primes p with p % 3 == 2.
part1 = {
    prime: {num for num in primes if num % 3 == 1 and compatible(prime, num)}
    for prime in primes
    if prime % 3 == 1
}
part2 = {
    prime: {num for num in primes if num % 3 == 2 and compatible(prime, num)}
    for prime in primes
    if prime % 3 == 2
}
compatibility = part1 | part2

candidates = []

for root, partners in compatibility.items():
    for p1, p2 in combinations(partners, 2):
        # Check each pair of numbers compatible with root:
        # 1. They have to be compatible to each other to form a trio.
        # 2. Their compatible numbers in turn have to have an intersection of at least
        # two more numbers.
        # 3. At least two numbers in this intersection have to be compatible with root
        # and with each other.

        # Checking one direction is enough because of symmetry
        if p1 not in compatibility[p2]:
            continue

        intersection = compatibility[p1] & compatibility[p2]
        # root will be in both lists, but we want at least two more
        if len(intersection) < 3:
            continue

        intersection_compatible_with_root = intersection & partners
        if len(intersection_compatible_with_root) < 2:
            continue

        for q1, q2 in combinations(intersection_compatible_with_root, 2):
            if q1 not in compatibility[q2]:
                continue
            candidates.append({root, p1, p2, q1, q2})


print(min(sum(candidate) for candidate in candidates))
