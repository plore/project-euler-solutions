def triangle(n: int) -> int:
    return int(n * (n + 1) / 2)


def penta(n: int) -> int:
    return int(n * (3 * n - 1) / 2)


def hexa(n: int) -> int:
    return n * (2 * n - 1)


num = 286
while True:
    # penta(num) is slightly less than 3 * triangle(num)
    # hexa(num) is slightly less 4 * triangle(num)
    m = int(num / 3**0.5)
    h = int(num / 2)

    while penta(m) < triangle(num):
        m += 1
    while hexa(h) < triangle(num):
        h += 1

    if penta(m) == triangle(num) and hexa(h) == triangle(num):
        print(triangle(num))
        break

    num += 1
