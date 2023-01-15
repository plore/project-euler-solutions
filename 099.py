from math import log

nums = []
exps = []
with open("099.txt", "r") as infile:
    for line in infile.readlines():
        num, exp = line.strip().split(",")
        nums.append(int(num))
        exps.append(int(exp))

log_values = [log(num) * exp for (num, exp) in zip(nums, exps)]
max_value = max(log_values)
print(log_values.index(max_value) + 1)
