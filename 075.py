from math import gcd

# Use Euclid's formula to generate triples from integers m > 0, n > 0:
# a = m^2 - n^2
# b = 2mn
# c = m^2 + n^2
# while m and and n are coprime and one of them is even.
# Also include multiples of a, b,c.
# Then L = k(a + b + c) = 2km(m + n).

limit = 1500000
num_solutions = [0] * (limit + 1)

max_n = int(limit / 4)

for n in range(1, max_n + 1):
    m = n + 1
    while 2 * m * (m + n) < limit:

        a = m**2 + n**2
        b = 2 * m * n
        c = m**2 - n**2
        assert a**2 == b**2 + c**2

        for k in range(1, int(limit / (a + b + c)) + 1):
            num_solutions[k * (a + b + c)] += 1

        # ensure coprimality and even-ness of either n or m
        m += 2
        while not gcd(n, m) == 1:
            m += 2

print(num_solutions.count(1))
