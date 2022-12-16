from math import ceil

# The base for exponentiation can't be more than 9 since 10^n always has n + 1 digits.
# On the other hand, 1^1, 2^1, 3^1, 4^1 etc. have 1 digit each.
# In general we want 10^(n - 1) <= x^n < 10^n or 10^((n - 1) / n) <= x < 10.
# We count the integer x satisfying this inequality for any given n, knowing that 10^(29/30) > 9 so no solutions exist for n bigger than 30.

count = 0
for n in range(1, 30):
    min_x = ceil(10 ** ((n - 1) / n))
    count += 10 - min_x

print(count)
