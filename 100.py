# If N is the number of all disks and M is the number of blue disks, we want
#     M / N * (M - 1) / (N - 1) = 1/2
# <=>       N^2 - N + 2M - 2M^2 = 0
#
# Solving for integer N we find that 8M^2 - 8M + 1 has to be a square.
#       8M^2 - 8M + 1 = X^2
# <=> 2(2M - 1)^2 - 1 = X^2
# <=>      X^2 - 2Y^2 = -1  with Y = 2M - 1
# which is a diophantine equation with trivial fundamental solution
# x = 1, y = 1
# and recurrence relation (positive and negative Pell's equation yield the same for n=2)
# x' = 3x + 4y
# y' = 2x + 3y

x, y = 1, 1
while (x + 1) / 2 < 1e12:
    x, y = 3 * x + 4 * y, 2 * x + 3 * y

print((y + 1) // 2)
