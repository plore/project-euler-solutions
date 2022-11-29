def get_factors(num: int) -> list[int]:
    factors = []
    for factor in range(1, int(num**0.5) + 1):
        if num % factor == 0:
            factors.append(factor)
            if num // factor != factor:
                factors.append(num // factor)

    return factors


assert sorted(set(get_factors(1))) == [1]
assert sorted(set(get_factors(2))) == [1, 2]
assert sorted(set(get_factors(3))) == [1, 3]
assert sorted(set(get_factors(4))) == [1, 2, 4]
assert sorted(set(get_factors(5))) == [1, 5]
assert sorted(set(get_factors(6))) == [1, 2, 3, 6]
assert sorted(set(get_factors(10))) == [1, 2, 5, 10]
assert sorted(set(get_factors(15))) == [1, 3, 5, 15]
assert sorted(set(get_factors(21))) == [1, 3, 7, 21]
assert sorted(set(get_factors(28))) == [1, 2, 4, 7, 14, 28]


triangle = 0
i = 1
while True:
    triangle += i
    i += 1
    factors = get_factors(triangle)
    if len(factors) > 500:
        print(triangle)
        break
