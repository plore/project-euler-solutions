from helpers import fraction_representation

odd_period_count = 0
for x in range(10000 + 1):
    if x**0.5 == int(x**0.5):
        continue

    _, cycle = fraction_representation(x)

    if len(cycle) % 2 == 1:
        odd_period_count += 1

print(odd_period_count)
