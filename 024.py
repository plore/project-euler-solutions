#  from itertools import permutations, islice
from math import factorial

# perm = next(islice(permutations(range(10)), 999999, 1000000))
# print("".join([str(i) for i in perm]))

# Alternative solution without "cheating"

# Fixing the first digit to 0, there are 9! permutations for the other digits.
# After running through those 9! permutations for the other digits, we increase the
# first digit to 1 and repeat.
# 2 * 9! < 1000000 <= 3 * 9!, therefore the first digit has to be 2.
# Starting with 0 (the lowest remaining digit) for the second position, there are 8!
# permutations for the other positions.
# 6 * 8! < 1000000 - 2 * 9! <= 7 * 8!, therefore the second digit is 6th lowest
# remaining, which is 7.
# Continue like this until the last digit is reached.

remaining_digits = list(range(10))
solution = []
rest = 1000000
while len(remaining_digits) > 0:
    fact = factorial(len(remaining_digits) - 1)
    digit_index = 0
    while rest > fact:
        digit_index += 1
        rest -= fact

    digit = remaining_digits[digit_index]
    solution.append(digit)
    remaining_digits.remove(digit)


print("".join([str(d) for d in solution]))
