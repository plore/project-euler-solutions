# In a 2 * n + 1 by 2 * n + 1 spiral there are n + 1 "layers"

# "Layer" zero
total = 1
current = 1
for n in range(500):
    # Collect diagonals in spiral "layer" n + 1
    for i in range(4):
        current += 2 * (n + 1)
        total += current

print(total)
