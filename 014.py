LIMIT = 1000000
lengths = [1] * LIMIT
for start_num in range(1, LIMIT):
    length = 0
    i = start_num
    # whenever i falls below start_num, we can stop and use knowledge gained
    # from a previous chain
    while i >= start_num and i != 1:
        length += 1
        i = i // 2 if i % 2 == 0 else 3 * i + 1
    length += lengths[i]
    lengths[start_num] = length

result = max((length, idx) for idx, length in enumerate(lengths))[1]
print(result)
