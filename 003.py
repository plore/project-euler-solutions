def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    for m in range(2, int(x**0.5) + 1):
        if x % m == 0:
            return False
    return True


number = 600851475143

print(
    next(
        factor
        for factor in range(int(number**0.5) + 1, 2, -1)
        if number % factor == 0 and is_prime(factor)
    )
)
