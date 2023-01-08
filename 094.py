# Calculating by brute force the first few side lengths a, we discover integer sequence
# https://oeis.org/A120893

a = 5
an = 1
ann = 1

max_sidelength = int(1e9 / 3)
perimeter_sum = 0

while a < max_sidelength:

    side_minus = (a**2 - (a - 1) ** 2 / 4) ** 0.5
    side_plus = (a**2 - (a + 1) ** 2 / 4) ** 0.5

    if side_minus.is_integer():
        perimeter_sum += 3 * a - 1
    elif side_plus.is_integer():
        perimeter_sum += 3 * a + 1
    else:
        raise Exception

    a_next = 3 * a + 3 * an - ann
    ann, an, a = an, a, a_next

print(perimeter_sum)
