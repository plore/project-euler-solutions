from itertools import permutations
from typing import Sequence

from helpers import to_num


def divisible(tup: Sequence[int], num: int) -> bool:
    return to_num(tup) % num == 0


total = 0
for x in permutations(range(10)):
    # pylint: disable=too-many-boolean-expressions
    if (
        x[3] % 2 == 0
        and (x[5] == 5 or x[5] == 0)
        and divisible(x[2:5], 3)
        and divisible(x[4:7], 7)
        and divisible(x[5:8], 11)
        and divisible(x[6:9], 13)
        and divisible(x[7:], 17)
    ):
        total += to_num(x)

print(total)
