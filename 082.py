def vertical_movement_sum(
    mat: list[list[int]], col: int, row_a: int, row_b: int
) -> int:
    min_row = min(row_a, row_b)
    max_row = max(row_a, row_b)
    return sum(mat[row][col] for row in range(min_row, max_row + 1))


matrix = []
with open("082.txt", "r") as infile:
    for line in infile.readlines():
        matrix.append([int(c) for c in line.strip().split(",")])

d = len(matrix)

# Initialization: since all matrix items are > 0 the minimal path to the leftmost column is the leftmost column itself.
minimal_path_sum = [[matrix[y][0]] + [0] * (d - 1) for y in range(d)]

for column in range(1, d):
    for row in range(0, d):
        # Moving from left to right, it might be cheaper to arrive from another row and incur vertical movement cost.
        minimal_path_sum[row][column] = min(
            minimal_path_sum[row_origin][column - 1]
            + vertical_movement_sum(matrix, column, row_origin, row)
            for row_origin in range(0, d)
        )


print(min(minimal_path_sum[row][-1] for row in range(d)))
