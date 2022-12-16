# use dynamic programming again

nums = []
sums = []
with open("067.txt", "r") as file:
    for line in file.readlines():
        nums.append([int(x) for x in line.strip().split(" ")])
        sums.append([0] * len(nums[-1]))

# initialization
sums[0][0] = nums[0][0]
for i in range(1, len(nums)):
    sums[i][0] = nums[i][0] + sums[i - 1][0]
    sums[i][i] = nums[i][i] + sums[i - 1][i - 1]

# iteration
for y in range(2, len(nums)):
    for x in range(1, len(nums[y]) - 1):
        sums[y][x] = max(sums[y - 1][x], sums[y - 1][x - 1]) + nums[y][x]

print(max(sums[len(sums) - 1]))
