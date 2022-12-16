from fractions import Fraction

n = 0
d = 1

cs = [int(2 * (k + 1) / 3) if k % 3 == 2 else 1 for k in range(1, 100)]
for c in cs[::-1]:
    # Work the way up the continued fraction:
    # n' / d = c + n / d, then invert
    n += c * d
    n, d = d, n

# Add integer part of e and simplify the fraction
n += 2 * d
n, d = Fraction(n, d).numerator, Fraction(n, d).denominator

print(sum(int(c) for c in str(n)))
