def penta(n: int) -> int:
    return n * (3 * n - 1) // 2


def is_penta(m: int) -> bool:
    n = (1 + (1 + 24 * m) ** 0.5) / 6  # From solving n(3n - 1)/2 = m for n
    return int(n) == n  # type: ignore[no-any-return]


num = 2
while True:
    pn = penta(num)
    # if P_m is smaller than P_n - P_{n-1}, P_n - P_m cannot be pentagonal
    difference_between_pentagonals = 3 * num - 2
    possible_partners = [
        penta(m) for m in range(num - 1) if penta(m) > difference_between_pentagonals
    ]
    diffs = [
        pn - pm for pm in possible_partners if is_penta(pn - pm) and is_penta(pn + pm)
    ]
    if len(diffs) > 0:
        print(int(min(diffs)))
        break
    num += 1
