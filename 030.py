# 999999 -> 6 * 9 ^ 5 = 354294
# Clearly, numbers higher than this always have a sum of digits fith powers smaller than the number itself

total = 0
for n in range(2, 354294):
    if sum(int(c) ** 5 for c in str(n)) == n:
        total += n

print(total)
