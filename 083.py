matrix = []
with open("083.txt", "r") as infile:
    for line in infile.readlines():
        matrix.append([int(c) for c in line.strip().split(",")])

d = len(matrix)
infinity = 10000 * d**2
minimal_path_sum = [[infinity] * d for _ in range(d)]
minimal_path_sum[0][0] = matrix[0][0]

current_min = minimal_path_sum[-1][-1]


# Pursue standard dynamic programming strategy, but iterate several times to allow for
# back-winding paths.
# Each step greedily optimizes from the four neighboring positions.
# Since we move from left to right and top to bottom, if any update occurs we know the
# bottom right sum will update as well.
def update(min_path_sum: list[list[int]], mat: list[list[int]]) -> None:
    for y in range(0, d):
        for x in range(0, d):
            if x == 0 and y == 0:
                continue

            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            min_path_sum[y][x] = mat[y][x] + min(
                min_path_sum[ny][nx]
                for (nx, ny) in neighbors
                if 0 <= nx < d and 0 <= ny < d
            )


while True:
    update(minimal_path_sum, matrix)
    if minimal_path_sum[-1][-1] == current_min:
        print(current_min)
        break
    current_min = minimal_path_sum[-1][-1]
