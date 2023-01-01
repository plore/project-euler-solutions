from collections import Counter


def order_relations(characters: str) -> set[tuple[int, int]]:
    a, b, c = [int(c) for c in characters]
    return {(a, b), (b, c), (a, c)}


relations = set()
with open("079.txt") as infile:
    for line in infile.readlines():
        relations |= order_relations(line.strip())


# We assume no digit occurs more than once.
# The more digits are preceded by x, the earlier x occcurs
preceding = Counter(first for first, _ in relations)
result = [digit for digit, _ in preceding.most_common()]

# Assuming no digit occurs more than once, one digit preceding no other digits is still missing
missing_digit = next(second for _, second in relations if second not in result)
result = result + [missing_digit]

print("".join(str(d) for d in result))
