from helpers import primes_up_to

# Use dynamic programming again:
# Define w[i][j] as the number of ways i can be written as a sum of the first j primes.
# Boundaries are trivial; going from j - 1 to j for number i we may add to w[i][j - 1]:
#   1               if i == p[j], in which case we use the jth prime for the first time
#   w[i - p[j]][j]  if i > p[j]
#   0               otherwise
#
# This leads to the following table for i <= 10:
#
#    |  2   3   5   7
# -------------------
#  1 |  0   0   0   0   ()
#  2 |  1   1   1   1   (2)
#  3 |  0   1   1   1   (3)
#  4 |  1   1   1   1   (2+2)
#  5 |  0   1   2   2   (2+3, 5)
#  6 |  1   2   2   2   (2+2+2, 3+3)
#  7 |  0   1   2   3   (3+2+2, 5+2, 7)
#  8 |  1   2   3   3   (2+2+2+2, 3+3+2, 5+3)
#  9 |  0   2   3   4   (3+3+3, 3+2+2+2, 5+2+2, 7+2)
# 10 |  1   2   4   5   (2+2+2+2+2, 3+3+2+2, 5+5, 5+3+2, 7+3)

# We assume the number of ways grows fast enough to reach 5000 ways with few primes.
p = primes_up_to(1000)
ways = [[0] * len(p) for i in [0, 1]]

i = 2
while i <= 100:
    ways.append([0] * len(p))
    ways[i][0] = 1 if i % p[0] == 0 else 0
    for j in range(1, len(p)):
        ways[i][j] = ways[i][j - 1]
        if i == p[j]:
            ways[i][j] += 1
        elif i > p[j]:
            ways[i][j] += ways[i - p[j]][j]

    if ways[i][-1] > 5000:
        break

    i += 1


assert ways[2][0] == 1
assert ways[3][0] == 0

assert ways[5][1] == 1
assert ways[5][2] == 2

assert ways[9][2] == 3
assert ways[9][3] == 4

assert ways[10][2] == 4
assert ways[10][3] == 5

print(i)
