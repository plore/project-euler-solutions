from math import gcd

# Always two cuboid faces have to be traversed, and from the 2D net it becomes clear that L**2 = a**2 + (b + c)**2 for path length L and dimensions a, b, c.
# This is minimized if a > b, c (the two shorter edges point in the same direction on the 2D net).
# Generate pythagorean triples L, a, (b + c) with a >= b >= c until there are over one million solutions a, b, c


def generate_triplets(limit: int) -> list[tuple[int, int, int]]:
    sols = []
    for n in range(1, int(limit / 4) + 1):
        m = n + 1
        while not gcd(n, m) == 1:
            m += 2
        while m * (m + n) < limit / 2:
            k = 1
            while 2 * k * m * (m + n) < limit:
                a = k * (m**2 + n**2)
                b = k * (2 * m * n)
                c = k * (m**2 - n**2)
                sols.append((a, b, c))
                k += 1
            m += 2
            while not gcd(n, m) == 1:
                m += 2
    return sols


target = 1000000

# Conservative guess how many triplets will be needed
all_triplets = generate_triplets(target)


def num_solutions(max_sidelength: int, triplets: list[tuple[int, int, int]]) -> int:
    _, values_a, values_bc = zip(*triplets)
    viable_sidelengths = [
        (a, bc)
        for a, bc in zip(values_a + values_bc, values_bc + values_a)
        if a <= max_sidelength and bc <= 2 * a
    ]
    count = 0
    for a, bc in viable_sidelengths:
        if a > max_sidelength:
            continue

        # Count the number of ways to split bc up into integer b and c, excluding symmetries
        if bc <= a:
            count += int(bc / 2)
        else:
            count += int(bc / 2) - (bc - a) + 1
    return count


assert num_solutions(99, all_triplets) == 1975
assert num_solutions(100, all_triplets) == 2060

M = 0
solutions = 0
while solutions < target:
    M += int((target - solutions) / 2000) + 1
    solutions = num_solutions(M, all_triplets)

print(M)
