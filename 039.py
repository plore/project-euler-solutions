# Starting from a^2 + b^2 = c^2 and p = a + b + c, one can solve for b
# b = (p^2 - 2ap) / (2p - 2a)
# Then count the number of integer solutions for a given p

solution_counts = []
for p in range(1001):
    count = 0
    for a in range(1, int(p / 2) + 1):
        b = (p**2 - 2 * p * a) / (2 * p - 2 * a)
        if b == int(b):
            count += 1
    solution_counts.append(count)

# We know there can only be one solution, therefore index is unambiguous
print(solution_counts.index(max(solution_counts)))
