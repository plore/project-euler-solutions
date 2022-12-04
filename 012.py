from helpers import get_factors

triangle = 0
i = 1
while True:
    triangle += i
    i += 1
    factors = get_factors(triangle)
    if len(factors) > 500:
        print(triangle)
        break
