def ways(amount: int, coins: list[int]) -> int:
    if amount == 0:
        return 1
    if coins == [1]:
        return 1
    total = 0
    for i, coin in enumerate(coins):
        rest = amount - coin
        total += ways(rest, [c for c in coins[i:] if c <= rest])
    return total


assert ways(0, [2, 1]) == 1
assert ways(1, [2, 1]) == 1
assert ways(2, [2, 1]) == 2
assert ways(3, [2, 1]) == 2
assert ways(4, [2, 1]) == 3
assert ways(4, [1]) == 1
assert ways(5, [2, 1]) == 3
assert ways(5, [5, 2, 1]) == 4
assert ways(6, [5, 2, 1]) == 5


# Alternative way: dynamic programming


def ways2() -> int:
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    way_grid = [[0] * len(coins) for i in range(201)]

    # There is always one way to create a total of zero (use no coins)
    for col, _ in enumerate(coins):
        way_grid[0][col] = 1

    for total in range(1, 201):
        for col, max_coin in enumerate(coins):
            if max_coin == 1:
                # There is only one way to have <total> with just 1p coins
                way_grid[total][col] = 1
            elif total < max_coin:
                # Can't use this coin yet, no extra ways
                way_grid[total][col] = way_grid[total][col - 1]
            else:
                # Can use one more of this coin
                way_grid[total][col] = (
                    way_grid[total][col - 1] + way_grid[total - max_coin][col]
                )

    return way_grid[200][-1]


assert ways2() == ways(200, [200, 100, 50, 20, 10, 5, 2, 1])

print(ways2())
