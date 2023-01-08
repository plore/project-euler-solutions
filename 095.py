# The sequence formed by iteratively summing the proper divisors of the previous number
# is called an aliquot sequence.
# For each starting number, we eventually either exceed the limit, encounter a number
# from an already known amicable chain (since aliquot-sum is a non-injective function),
# or encounter a previous number from the current sequence, forming a new amicable chain

limit = 1000000
aliquot_sums = [0] * (limit + 1)
for div in range(1, limit // 2):
    for q in range(2, limit // div + 1):
        aliquot_sums[div * q] += div

chain_lengths = [0] * (limit + 1)
max_len = 0

max_chain = []

for n in range(2, limit):
    if chain_lengths[n] > 0:
        continue

    sequence = [n]
    next_num = aliquot_sums[n]
    while True:
        if next_num > limit:
            for c in sequence:
                chain_lengths[c] = -1
            break

        if next_num < n:
            for c in sequence:
                chain_lengths[c] = chain_lengths[next_num]
            break

        chain_start_index = next(
            (idx for idx, num in enumerate(sequence) if num == next_num), -1
        )
        if chain_start_index == -1:
            sequence.append(next_num)
            next_num = aliquot_sums[next_num]
            continue

        # A new chain has been discovered.
        for c in sequence:
            chain_lengths[c] = len(sequence) - chain_start_index
        if chain_lengths[n] > max_len:
            max_len = chain_lengths[n]
            max_chain = sequence[chain_start_index:]
        break


print(min(max_chain))
