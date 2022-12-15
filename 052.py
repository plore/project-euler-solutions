def digits(n: int) -> list[int]:
    return sorted(str(n))


x = 1
while not (
    digits(x) == digits(2 * x)
    and digits(x) == digits(3 * x)
    and digits(x) == digits(4 * x)
    and digits(x) == digits(5 * x)
    and digits(x) == digits(6 * x)
):
    x += 1

print(x)
