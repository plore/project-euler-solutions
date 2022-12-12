from helpers import is_prime


def truncatable_from_left(x: int) -> bool:
    n = len(str(x))
    for m in range(n):
        left_trunc = x % 10 ** (n - m)
        if not is_prime(left_trunc):
            return False
    return True


assert truncatable_from_left(2)
assert truncatable_from_left(3)
assert not truncatable_from_left(4)
assert truncatable_from_left(5)
assert truncatable_from_left(7)
assert not truncatable_from_left(11)
assert truncatable_from_left(13)
assert not truncatable_from_left(77)
assert truncatable_from_left(97)
assert truncatable_from_left(797)
assert truncatable_from_left(3797)


truncatable_from_right = [2, 3, 5, 7]
allowed_last_digits = [1, 3, 7, 9]

result = set()
while len(result) < 11:
    truncatable_from_right = [
        10 * a + b
        for a in truncatable_from_right
        for b in allowed_last_digits
        if is_prime(10 * a + b)
    ]
    result |= {num for num in truncatable_from_right if truncatable_from_left(num)}

print(sum(result))
