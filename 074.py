from math import factorial

facs = [factorial(x) for x in range(10)]

lengths = [0] * 1000000
lengths[169] = lengths[363601] = lengths[1454] = 3
lengths[871] = lengths[45361] = 2
lengths[872] = lengths[45362] = 2


def non_repeating_chain_length(start: int, chain_lengths: list[int]) -> int:
    current = start
    last = 0
    length = 0
    while True:
        if current == last:
            break
        if current < len(chain_lengths) and chain_lengths[current] > 0:
            length += chain_lengths[current]
            break
        last = current
        current = sum(facs[int(c)] for c in str(current))
        length += 1
    return length


assert non_repeating_chain_length(69, lengths) == 5
assert non_repeating_chain_length(78, lengths) == 4
assert non_repeating_chain_length(540, lengths) == 2

for n in range(1, 1000000):
    lengths[n] = non_repeating_chain_length(n, lengths)

print(len([length for length in lengths if length == 60]))
