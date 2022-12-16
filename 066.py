from fractions import Fraction
from itertools import chain, cycle

from helpers import fraction_representation

# x^2 - D * y^2 = 1 <=> (x^2 - 1) / y^2 = D => sqrt(D) can be approximated by x / y.
# We know from problem 65 that continued fractions provide the best approximations.


def frac(chainfrac_coeffs: list[int]) -> tuple[int, int]:
    n = 0
    d = 1
    for k in chainfrac_coeffs[::-1]:
        n += k * d
        n, d = Fraction(n, d).denominator, Fraction(n, d).numerator
    n, d = Fraction(n, d).denominator, Fraction(n, d).numerator
    return n, d


max_x = max_w = 1

for w in range(2, 1001):
    if w**0.5 == int(w**0.5):
        continue

    non_repeat, repeat = fraction_representation(w)
    coefficient_generator = chain(non_repeat, cycle(repeat))

    coeffs = []
    x, y = 1, 1
    while not 1 + w * y**2 == x**2:
        coeffs.append(next(coefficient_generator))
        x, y = frac(coeffs)
    if x > max_x:
        max_x = x
        max_w = w

print(max_w)
