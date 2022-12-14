from helpers import prime_factors

x = 2
while True:
    if all(len(set(prime_factors(num))) > 3 for num in [x, x + 1, x + 2, x + 3]):
        print(x)
        break
    x += 1
