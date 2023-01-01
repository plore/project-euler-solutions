from math import gcd

nums = []
dens = []
for n in range(11, 100):
    for d in range(n + 1, 100):
        n0, n1 = divmod(n, 10)
        d0, d1 = divmod(d, 10)
        # Cancelling both ones or both tens can never result in the same value unless
        # the fraction equals 1.
        # Therefore, we need to check only for crosswise cancelling
        if n0 == d1 and n1 * d == n * d0:
            nums.append(n)
            dens.append(d)
        if n1 == d0 and n0 * d == n * d1:
            nums.append(n)
            dens.append(d)

dprod = nprod = 1
for (
    n,
    d,
) in zip(nums, dens):
    nprod *= n
    dprod *= d

print(int(dprod / gcd(nprod, dprod)))
