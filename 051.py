from collections import Counter

from helpers import is_prime, primes_up_to

# To yield eight primes, only three or six or nine, etc. digits may be replaced.
# Otherwise, three out of ten numbers generated will be divisible by three.

# Bold claim: the desired primes will contain at most six digits.
# Start by focusing on primes with three identical digits and try all replacements.
# Some members of the family will have more than three identical digits, but with at
# most three different digits in non-replacement positions, at least 8 - 3 = 5 family
# members will have distinct digits between replacement and non-replacement positions.
primes = primes_up_to(1000000)

for p in primes:
    digit, frequency = Counter(str(p)).most_common(1)[0]
    replacement_positions = [idx for idx, d in enumerate(str(p)) if d == digit]
    if 6 in replacement_positions:
        continue  # No way to produce eight primes by replacing the last digit
    if 0 in replacement_positions:
        try_digits = range(1, 10)  # Leading zero not allowed
    else:
        try_digits = range(10)

    potential_family = [
        int(str(p).replace(digit, str(replacement_digit)))
        for replacement_digit in try_digits
    ]
    prime_family = [num for num in potential_family if is_prime(num)]
    if len(prime_family) > 7:
        print(min(prime_family))
        break
