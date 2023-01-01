def num_rectangles(dim_x: int, dim_y: int) -> int:
    res = 0
    # For each rectangle with shape (x, y), count how many positions the lower right
    # corner can occupy.
    for y in range(1, dim_y + 1):
        for x in range(1, dim_x + 1):
            res += (dim_y - y + 1) * (dim_x - x + 1)
    return res


assert num_rectangles(1, 1) == 1
assert num_rectangles(2, 1) == 3
assert num_rectangles(1, 2) == 3
assert num_rectangles(2, 2) == 9
assert num_rectangles(3, 2) == 18


# A grid of dimensions 1x2000 has 2001000 rectangles (2000 + 1999 + ... + 1).
# This yields 2000 as the maximal extent and a starting epsilon for the nearest solution
eps = 1000
closest_area = 2001000

for dimx in range(1, 2000):
    for dimy in range(1, dimx + 1):
        num = num_rectangles(dimx, dimy)
        if num > 2000000 + eps:
            break
        if abs(num - 2000000) < eps:
            eps = abs(num - 2000000)
            closest_area = dimx * dimy

print(closest_area)
