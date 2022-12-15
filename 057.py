# Expressing the ith iteration as a / b, by applying the iteration we get the (i+1)th iteration as (a + 2b) / (a + b)

count = 0
a = 3
b = 2
for j in range(1000):
    a, b = a + 2 * b, a + b
    if len(str(a)) > len(str(b)):
        count += 1

print(count)
