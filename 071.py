from math import gcd

reduced_fractions: list[tuple[int, int]] = []
for d in range(1, 1000000 + 1):
    if d % 7 == 0:
        low = int(3 / 7 * d) - 1
    else:
        low = int(3 / 7 * d)

    n = low
    while n / d < 3 / 7:
        reduced_n, reduced_d = int(n / gcd(n, d)), int(d / gcd(n, d))
        reduced_fractions.append((reduced_n, reduced_d))
        n += 1


closest_fraction = sorted(reduced_fractions, key=lambda tup: tup[0] / tup[1])[-1]
print(closest_fraction[0])
