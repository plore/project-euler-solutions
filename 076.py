N = 100

# memoization cache
F = [[-1] * (N + 1) for i in range(N + 1)]

# edge cases: only one decomposition of 1 and only one way to decompose i with 1s
for i in range(1, N + 1):
    F[1][i] = 1
    F[i][1] = 1


def num_decompositions(total: int, max_num: int) -> int:
    if total < 0:  # invalid decompositions
        return 0
    if total == 0:  # decomposition complete, recursion stop
        return 1
    if max_num > total:  # can't have individual summands bigger than the sum
        return num_decompositions(total, total)
    if F[total][max_num] > -1:  # rely on cache
        return F[total][max_num]
    # recurse with all possible biggest summands
    res = sum(num_decompositions(total - i, i) for i in range(1, max_num + 1))
    F[total][max_num] = res
    return res


# subtract one to exclude (non-)composition with only one summand
print(num_decompositions(N, N) - 1)
