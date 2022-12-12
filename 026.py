def cycle_length(denominator: int) -> int:
    rest_values = [1]
    rest = 1
    while True:
        if rest == 0:
            return 0  # 1 / denominator has a finite decimal representation
        while rest < denominator:
            rest *= 10
        rest %= denominator
        # check for cycle: the same rest as seen before will lead to the same sequence again
        for i, rest_value in enumerate(rest_values):
            if rest_value == rest:
                return len(rest_values) - i
        rest_values.append(rest)


assert cycle_length(1) == 0
assert cycle_length(2) == 0
assert cycle_length(3) == 1
assert cycle_length(4) == 0
assert cycle_length(5) == 0
assert cycle_length(6) == 1
assert cycle_length(7) == 6

maxd = 0
maxlen = 0
for d in range(5, 1000):
    if cycle_length(d) > maxlen:
        maxlen = cycle_length(d)
        maxd = d

print(maxd)
