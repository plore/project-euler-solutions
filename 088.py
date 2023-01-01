from helpers import is_prime


def recursive_product_partitions(n: int) -> list[list[int]]:
    res = [[n]]
    if is_prime(n):
        return res

    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            for p in recursive_product_partitions(n // d):
                res.append(sorted(p + [d]))
    return res


def make_product_partitions(n: int) -> set[tuple[int, ...]]:
    return set(tuple(partition) for partition in recursive_product_partitions(n)[1:])


assert make_product_partitions(1) == set()
assert make_product_partitions(2) == set()
assert make_product_partitions(3) == set()
assert make_product_partitions(4) == {(2, 2)}
assert make_product_partitions(6) == {(2, 3)}
assert make_product_partitions(8) == {(2, 4), (2, 2, 2)}
assert make_product_partitions(12) == {(2, 2, 3), (2, 6), (3, 4)}


# From each product partition of n we can construct a product-sum set of k numbers by
# appending a certain number of ones.
def reachable_k(n: int) -> list[int]:
    res = []
    for pp in make_product_partitions(n):
        number_of_ones = n - sum(pp)
        res.append(len(pp) + number_of_ones)
    return res


# For any k thus reached the first n is minimal, therefore we only need to increase n
# until all desired k have been reached.

inf = 1000000
minnums = [inf] * 12000
num = 2
while max(minnums[2:]) == inf:
    for k in reachable_k(num):
        if k < 12000 and num < minnums[k]:
            minnums[k] = num
    num += 1


assert minnums[2:7] == [4, 6, 8, 8, 12]
assert set(minnums[2:13]) == {4, 6, 8, 12, 15, 16}

print(sum(set(minnums[2:])))
