from itertools import combinations
from typing import Iterable

d1 = list(combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6))
d2 = list(combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6))

d1_extended = []
count = 0
for x in d1:
    if 6 in x and 9 not in x:
        d1_extended.append(x + (9,))
    elif 9 in x and 6 not in x:
        d1_extended.append(x + (6,))
    else:
        d1_extended.append(x)

d2_extended = d1_extended.copy()


def can_display_all_squares(dice1: Iterable[int], dice2: Iterable[int]) -> bool:
    squares = [(0, 1), (0, 4), (0, 9), (1, 6), (2, 5), (3, 6), (4, 9), (6, 4), (8, 1)]
    for digit1, digit2 in squares:
        if not (
            (digit1 in dice1 and digit2 in dice2)
            or (digit1 in dice2 and digit2 in dice1)
        ):
            return False

    return True


assert can_display_all_squares([0, 5, 6, 7, 8, 9], [1, 2, 3, 4, 6, 8, 9])
assert can_display_all_squares([0, 5, 6, 7, 8, 9], [1, 2, 3, 4, 6, 7, 9])
assert not can_display_all_squares([1, 2, 3, 4, 5, 6, 9], [1, 2, 3, 4, 5, 6, 9])

for config1 in d1_extended:
    for config2 in d2_extended:
        if can_display_all_squares(config1, config2):
            count += 1

# By iterating over the product of combinations but allowing both dice to be in either
# position we found each arrangement twice.
print(count // 2)
