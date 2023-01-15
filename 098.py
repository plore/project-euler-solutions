from collections import Counter
from itertools import combinations, permutations


def is_anagram(a: str, b: str) -> bool:
    return len(a) == len(b) and Counter(a) == Counter(b)


def is_square(x: int) -> bool:
    return (x**0.5).is_integer()  # type: ignore[no-any-return]


with open("098.txt", "r") as infile:
    words = [word.strip('"') for word in infile.read().split(",")]

anagram_pairs = [(wa, wb) for wa, wb in combinations(words, 2) if is_anagram(wa, wb)]


maxsquare = 0

for wa, wb in anagram_pairs:
    letters = []
    for c in wa:
        if c not in letters:
            letters.append(c)
    for digits in permutations("0123456789", len(letters)):
        translation = str.maketrans(dict(zip(letters, digits)))
        trans_a = wa.translate(translation)
        trans_b = wb.translate(translation)
        if trans_a.startswith("0") or trans_b.startswith("0"):
            continue

        num_a = int(trans_a)
        num_b = int(trans_b)
        if is_square(num_a) and is_square(num_b):
            maxsquare = max(maxsquare, num_a, num_b)

print(maxsquare)
