from typing import Generator
from itertools import islice


def get_factors(num: int, include_num: bool = True) -> list[int]:
    factors = [1] if num > 1 else []
    if include_num:
        factors.append(num)
    for factor in range(2, int(num**0.5) + 1):
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

assert sorted(set(get_factors(1, include_num=False))) == []
assert sorted(set(get_factors(28, include_num=False))) == [1, 2, 4, 7, 14]


def primes_up_to(max_num: int) -> list[int]:
    if max_num <= 1:
        return []

    nums = list(range(1, max_num + 1))
    for i in range(1, int(max_num**0.5) + 1):
        if nums[i] == 0:
            continue

        for j in range(2, int(max_num / nums[i]) + 1):
            nums[nums[i] * j - 1] = 0

    return [num for num in nums if num != 0 and num > 1]


assert primes_up_to(-42) == []
assert primes_up_to(0) == []
assert primes_up_to(1) == []
assert primes_up_to(2) == [2]
assert primes_up_to(3) == [2, 3]
assert primes_up_to(17) == [2, 3, 5, 7, 11, 13, 17]
assert primes_up_to(18) == [2, 3, 5, 7, 11, 13, 17]
assert primes_up_to(19) == [2, 3, 5, 7, 11, 13, 17, 19]


def fibonacci() -> Generator[int, None, None]:
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


assert list(islice(fibonacci(), 10)) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
