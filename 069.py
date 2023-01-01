# Any integer n > 1 can be expressed as p1 ^ m1 * ... * pk ^ mk with prime factors
# p1 ... pk occurring m1 ... mk times, respectively.
# The totient phi(n) = p1 ^ (m1 - 1) * (p1 - 1) * ... * pk ^ (mk - 1) * (pk - 1).
# Thus n / phi(n) can be expressed as p1 / (p1 - 1) * ... * pk / (pk - 1) where the
# m1 ... mk have become irrelevant.
# Hence, n / phi(n) is maximized by using as many unique and small primes as possible.

print(2 * 3 * 5 * 7 * 11 * 13 * 17)
