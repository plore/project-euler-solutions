# geometrical insights: Call the points O, P = (xP, yP) and Q = (xQ, yQ). Then
# 1) To prevent double counting, yP / xP > yQ / xQ
# 2) If xP > xQ, the line from Q to P has positive slope and no right angle is possible
# 3) Therefore, xQ = 0 forces the triangle onto the line x = 0 and can be excluded


def right_triangles_from_origin(
    lower_right_coordinate: tuple[int, int], max_y: int
) -> int:
    xQ, yQ = lower_right_coordinate
    count = 0
    for xP in range(0, xQ + 1):
        min_y = int(yQ / xQ * xP + 1e-5) + 1
        for yP in range(min_y, max_y + 1):
            a = (yP - yQ) ** 2 + (xP - xQ) ** 2
            b = yP**2 + xP**2
            c = yQ**2 + xQ**2
            if a + b == c or a + c == b or b + c == a:
                count += 1
    return count


assert right_triangles_from_origin((1, 0), 1) == 2
assert right_triangles_from_origin((1, 1), 1) == 1

assert right_triangles_from_origin((1, 0), 2) == 4
assert right_triangles_from_origin((2, 0), 2) == 5
assert right_triangles_from_origin((1, 1), 2) == 2
assert right_triangles_from_origin((2, 1), 2) == 1
assert right_triangles_from_origin((1, 2), 2) == 1
assert right_triangles_from_origin((2, 2), 2) == 1


count = 0
limit = 50
for xQ in range(1, limit + 1):
    for yQ in range(0, limit + 1):
        count += right_triangles_from_origin((xQ, yQ), limit)

print(count)
