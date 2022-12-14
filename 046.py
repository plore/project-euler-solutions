from helpers import is_prime


def goldbach_writable(n: int) -> bool:
    for m in range(1, int((n / 2) ** 0.5 + 1)):
        if is_prime(n - 2 * m**2):
            return True
    return False


assert goldbach_writable(9)
assert goldbach_writable(15)
assert goldbach_writable(21)
assert goldbach_writable(25)
assert goldbach_writable(27)
assert goldbach_writable(31)
assert not goldbach_writable(17)

num = 33
while True:
    num += 2
    if is_prime(num):
        continue

    if not goldbach_writable(num):
        print(num)
        break
