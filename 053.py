from math import comb

count = 0
for n in range(1, 101):
    for r in range(n + 1):
        if comb(n, r) > 1000000:
            count += 1

print(count)
