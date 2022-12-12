from math import factorial

factorials = {n: factorial(n) for n in range(0, 10)}

total = 0
# Since 7 * 9! < 9999999, higher numbers don't have to be checked as they would produce an even smaller ratio
for n in range(3, 7 * factorial(9)):
    facsum = sum(factorials[int(c)] for c in str(n))
    if facsum == n:
        total += n

print(total)
