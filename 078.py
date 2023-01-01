N = 100000

# Use Euler's pentagonal number theorem


def penta(m: int) -> int:
    return int(m / 2 * (3 * m - 1))


assert penta(-4) == 26
assert penta(-3) == 15
assert penta(-2) == 7
assert penta(-1) == 2
assert penta(0) == 0
assert penta(1) == 1
assert penta(2) == 5
assert penta(3) == 12
assert penta(4) == 22


p = [1]

n = 1
while True:
    pn = 0

    k = 1
    while True:
        idx = n - penta(k)
        if idx < 0:
            break
        pn += int((-1) ** (k - 1)) * p[idx]
        k += 1

    k = -1
    while True:
        idx = n - penta(k)
        if idx < 0:
            break
        pn += int((-1) ** (k - 1)) * p[idx]
        k -= 1

    p.append(pn)

    if pn % 1000000 == 0:
        print(n)
        break

    n += 1
