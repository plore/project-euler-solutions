from helpers import get_factors

total = 0
for n in range(1, 10000):
    d = int(sum(get_factors(n, include_num=False)))
    # if smaller than n we would have encountered d sooner as an amicable partner
    if n < d < 10000 and sum(get_factors(d, include_num=False)) == n:
        total += n + d

print(total)
