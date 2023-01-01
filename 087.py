from helpers import primes_up_to

limit = 50000000
primes = primes_up_to(int(limit**0.5))

second_powers = [p**2 for p in primes if p**2 < limit]
third_powers = [p**3 for p in primes if p**3 < limit]
fourth_powers = [p**4 for p in primes if p**4 < limit]

expressible_numbers = set()

for x in second_powers:
    for y in third_powers:
        if x + y > limit:
            break
        for z in fourth_powers:
            if x + y + z >= limit:
                break
            expressible_numbers.add(x + y + z)

print(len(expressible_numbers))
