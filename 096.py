Grid = list[list[int]]


def valid(grid: Grid, x: int, y: int) -> bool:
    return valid_block(grid, x, y) and valid_row(grid, x, y) and valid_col(grid, x, y)


def valid_block(grid: Grid, x: int, y: int) -> bool:
    range_x = range((x // 3) * 3, (x // 3 + 1) * 3)
    range_y = range((y // 3) * 3, (y // 3 + 1) * 3)
    num = grid[y][x]
    other_nums = [grid[j][i] for i in range_x for j in range_y if (i, j) != (x, y)]
    return num not in other_nums


def valid_row(grid: Grid, x: int, y: int) -> bool:
    num = grid[y][x]
    other_nums = [grid[y][i] for i in range(9) if i != x]
    return num not in other_nums


def valid_col(grid: Grid, x: int, y: int) -> bool:
    num = grid[y][x]
    other_nums = [grid[i][x] for i in range(9) if i != y]
    return num not in other_nums


def find_next_free_position(
    grid: Grid, x: int, y: int
) -> tuple[int | None, int | None]:
    for j in range(y, 9):
        min_x = x if j == y else 0
        for i in range(min_x, 9):
            if grid[j][i] == 0:
                return i, j
    return None, None


def possible_numbers(grid: Grid, x: int, y: int) -> set[int]:
    row_numbers = set(grid[y][i] for i in range(9))
    col_numbers = set(grid[j][x] for j in range(9))

    range_x = range((x // 3) * 3, (x // 3 + 1) * 3)
    range_y = range((y // 3) * 3, (y // 3 + 1) * 3)
    block_numbers = set(grid[j][i] for i in range_x for j in range_y)

    return set(range(1, 10)) - row_numbers - col_numbers - block_numbers


# Solve via backtracking
def solve(grid: Grid, from_x: int, from_y: int) -> bool:
    x, y = find_next_free_position(grid, from_x, from_y)
    if x is None or y is None:
        return True

    for num in possible_numbers(grid, x, y):
        grid[y][x] = num
        if valid(grid, x, y) and solve(grid, x, y):
            return True
        grid[y][x] = 0
    return False


def solve_sudoku(initial_grid: Grid) -> None:
    res = solve(initial_grid, 0, 0)
    assert res


grids = []
current_grid: Grid = []
with open("096.txt", "r") as infile:
    for line in infile.readlines():
        if line.startswith("Grid"):
            if current_grid:
                grids.append(current_grid)
            current_grid = []
        else:
            current_grid.append([int(c) for c in line.strip()])
    grids.append(current_grid)

total = 0
for idx, g in enumerate(grids):
    solve_sudoku(g)
    code = g[0][0] * 100 + g[0][1] * 10 + g[0][2]
    if idx == 0:
        assert code == 483
    total += code

print(total)
