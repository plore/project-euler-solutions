from collections import defaultdict

# Map numbers n to the "cube id" - the ordered list of digits of n^3
# Increase n until we encounter a cube id five times


def cube_id(num: int) -> str:
    return "".join(sorted(str(num**3)))


cubes = defaultdict(list)
n = 1
while True:
    cid = cube_id(n)
    cubes[cid].append(n)
    if len(cubes[cid]) == 5:
        print(min(m**3 for m in cubes[cid]))
        break
    n += 1
