from itertools import permutations
from typing import Sequence


def is_valid(perm: Sequence[int]) -> bool:
    line_sum = perm[4] + perm[9] + perm[5]
    return all(perm[i] + perm[i + 5] + perm[i + 6] == line_sum for i in range(4))


maxstring = 0
for p in permutations(range(1, 11)):
    if not is_valid(p):
        continue

    triplets = [(p[i], p[i + 5], p[5 + (i + 1) % 5]) for i in range(5)]

    outer_nodes = [t[0] for t in triplets]
    min_index = outer_nodes.index(min(outer_nodes))
    triplets = triplets[min_index:] + triplets[:min_index]

    string = "".join([f"{t[0]}{t[1]}{t[2]}" for t in triplets])
    if len(string) == 16:
        maxstring = max(maxstring, int(string))

print(maxstring)
