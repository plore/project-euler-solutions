from helpers import get_factors

abundants = [n for n in range(1, 28124) if sum(get_factors(n, include_num=False)) > n]

nonexpressable = list(range(0, 28123 * 2 + 1))
for idx, a in enumerate(abundants):
    for b in abundants[idx:]:
        nonexpressable[a + b] = 0

print(sum(nonexpressable[:28123]))
