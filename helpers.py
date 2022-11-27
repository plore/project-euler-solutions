def primes_up_to(max_num: int) -> list[int]:
    if max_num <= 1:
        return []

    nums = list(range(1, max_num + 1))
    for i in range(1, int(max_num ** 0.5) + 1):
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
assert primes_up_to(17) == [2,3,5,7,11,13,17]
assert primes_up_to(18) == [2,3,5,7,11,13,17]
assert primes_up_to(19) == [2,3,5,7,11,13,17,19]
