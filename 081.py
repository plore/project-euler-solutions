def find_minimal_path_sum_to(y: int, x: int, min_sums: list[list[int]]) -> int:
    if y == 0 and x == 0:
        return 0
    if y == 0 and x > 0:
        return min_sums[y][x - 1]
    if y > 0 and x == 0:
        return min_sums[y - 1][x]
    left = min_sums[y][x - 1]
    upper = min_sums[y - 1][x]
    return min(left, upper)


matrix = []
with open("081.txt", "r") as infile:
    for line in infile.readlines():
        matrix.append([int(num) for num in line.strip().split(",")])

num_rows = len(matrix)
num_cols = len(matrix[0])

minimal_path_sums = [[-1] * num_cols for i in range(num_rows)]

for row in range(num_rows):
    for col in range(num_cols):
        minimal_path_sums[row][col] = (
            find_minimal_path_sum_to(row, col, minimal_path_sums) + matrix[row][col]
        )

print(minimal_path_sums[-1][-1])
