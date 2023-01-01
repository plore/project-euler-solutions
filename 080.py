def sqrt_digits(num: int, steps: int) -> list[int]:
    if int(num**0.5) == num**0.5:
        return [int(num**0.5)]

    # We can approximate, for any integer n, sqrt(n) = 10(a + 10(b + 10(c + ...))))
    # with real a, b, c, ...
    # Approximation strategy for 1 < n < 100:
    # 0. p(0) = 0, c(0) = n
    # 1. Find the largest int x so that c(i) - (x^2 + 20xp(i)) > 0; x is the next digit
    # 2. c(i+1) = 100(c(i) - (x^2 + 20xp(i)))
    # 3. p(i+1) = 10p(i) + x
    #
    # From step 3, after k steps we can express p(k) with as (x(0), x(1), ..., x(k-1))

    res = []
    p = 0
    c = num
    for _ in range(steps):
        # find largest integer x so that x(20p + x) < c
        x = 1 if p == 0 else int(c / (20 * p))
        while x * (20 * p + x) < c:
            x += 1
        while x * (20 * p + x) > c:
            x -= 1
        res.append(x)

        c = 100 * (c - x * (20 * p + x))

        p = 10 * p + x

    return res


assert sqrt_digits(2, 10) == [1, 4, 1, 4, 2, 1, 3, 5, 6, 2]
assert sqrt_digits(2, 11) == [1, 4, 1, 4, 2, 1, 3, 5, 6, 2, 3]
assert sum(sqrt_digits(2, 100)) == 475
assert sqrt_digits(4, 1337) == [2]


digits = [sqrt_digits(n, 100) for n in range(1, 100)]
print(sum(sum(d) for d in digits if len(d) > 1))
