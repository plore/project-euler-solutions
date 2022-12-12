from itertools import permutations

# For each permutation of the digits, assign the first few to x, the next few to y and the last few to z and check for x * y == z.
# 987 is the highest potential 3-digit z but the smallest possible product from remaining digits is 1 * 23456 > 987.
# Likewise, 12345 is the smallest potential 5-digit z but the highest possible product from remaining digits is 96 * 87 < 12345.
# Therefore z has to consist of four digits.
# By assigning the remaining five digits either x * yyyy or xx * yyy, some duplication can be avoided.


products = set()
for p in permutations(range(1, 10)):
    for i in [1, 2]:
        x = int("".join(map(str, p[:i])))
        y = int("".join(map(str, p[i:5])))
        z = int("".join(map(str, p[5:])))
        if x * y == z:
            products.add(z)

print(sum(products))
