def is_triangle(t: int) -> bool:
    n = (1 + (1 + 8 * t) ** 0.5) / 2  # From solving n(n+1)/2 = t for n
    return n == int(n)  # type: ignore[no-any-return]


assert is_triangle(1)
assert is_triangle(3)
assert is_triangle(6)
assert is_triangle(10)
assert is_triangle(15)
assert is_triangle(21)
assert is_triangle(55)

assert not is_triangle(2)
assert not is_triangle(4)
assert not is_triangle(11)


with open("042.txt", "r") as f:
    words = f.read().replace('"', "").split(",")

triangle_words = [w for w in words if is_triangle(sum(ord(x) - 64 for x in w))]

print(len(triangle_words))
