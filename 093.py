from itertools import combinations, permutations, product
from operator import add, mul, sub
from typing import Iterable


def div(x: float, y: float) -> float:
    return 0 if y == 0 else x / y


funcs = [add, sub, mul, div]


def generate_ints(x1: int, x2: int, x3: int, x4: int) -> set[int]:
    res = []
    for a, b, c, d in permutations([x1, x2, x3, x4]):
        for op1, op2, op3 in product(funcs, repeat=3):
            results = [
                op3(op2(op1(a, b), c), d),  # ((a . b) . c ). d
                op3(op1(a, op2(b, c)), d),  # (a . (b . c)) . d
                op1(a, op3(op2(b, c), d)),  # a . ((b . c) . d)
                op1(a, op2(b, op3(c, d))),  # a . (b . (c . d))
                op2(op1(a, b), op3(c, d)),  # (a . b) . (c . d)
            ]
            res.extend([round(f) for f in results if f > 0 and abs(f - int(f)) < 1e-10])
    return set(res)


assert len(generate_ints(1, 2, 3, 4)) == 31
assert all(n in generate_ints(1, 2, 3, 4) for n in range(1, 29))

max_n = 0
max_seq: Iterable[int] = []
for digits in combinations(range(10), 4):
    ints = generate_ints(*digits)
    idx_and_num = enumerate(sorted(ints))
    n = sum(1 for idx, num in idx_and_num if idx + 1 == num)
    if n > max_n:
        max_n = n
        max_seq = digits

print("".join([str(i) for i in max_seq]))
