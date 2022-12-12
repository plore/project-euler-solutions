from helpers import is_prime, primes_up_to


def rot_one(num: int) -> int:
    n = len(str(num))
    return (num % 10 ** (n - 1)) * 10 + num // 10 ** (n - 1)  # type: ignore[no-any-return]


def circular_prime(num: int) -> bool:
    if num in [2, 3, 5, 7]:
        return True
    s = str(num)
    if any([digit in s for digit in "024568"]):
        return False
    for r in range(len(s) - 1):
        num = rot_one(num)
        if not is_prime(num):
            return False
    return True


primes = primes_up_to(1000000)

count = len([p for p in primes if circular_prime(p)])

print(count)
