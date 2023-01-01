from itertools import permutations


def triangle(n: int) -> int:
    return int(n * (n + 1) / 2)


def square(n: int) -> int:
    return n**2


def penta(n: int) -> int:
    return int(n * (3 * n - 1) / 2)


def hexa(n: int) -> int:
    return n * (2 * n - 1)


def hepta(n: int) -> int:
    return int(n * (5 * n - 3) / 2)


def octa(n: int) -> int:
    return n * (3 * n - 2)


# Triangle number grow the slowest and triangle(200) = 20100 has five digits already
nums = [
    [func(x) for x in range(200) if len(str(func(x))) == 4]
    for func in [triangle, square, penta, hexa, hepta, octa]
]

perms = list(permutations([0, 1, 2, 3, 4, 5]))[:120]


def cycle(first: int, second: int) -> bool:
    return int(str(first)[-2:]) == int(str(second)[:2])


def find_result() -> int:
    # pylint: disable=too-many-nested-blocks
    for p0, p1, p2, p3, p4, p5 in perms:
        for a in nums[p0]:
            for b in [x for x in nums[p1] if cycle(a, x)]:
                for c in [x for x in nums[p2] if cycle(b, x)]:
                    for d in [x for x in nums[p3] if cycle(c, x)]:
                        for e in [x for x in nums[p4] if cycle(d, x)]:
                            for f in [x for x in nums[p5] if cycle(e, x)]:
                                if cycle(f, a):
                                    # We know there can only be one
                                    return a + b + c + d + e + f
    return -1


print(find_result())
