from collections import defaultdict

squares = {str(i): i**2 for i in range(10)}


def iterate(num: int) -> int:
    return sum(squares[c] for c in str(num))


def arrival_number(num: int, all_arrival_numbers: dict[int, int]) -> int:
    while num not in (1, 89):
        if all_arrival_numbers[num] != 0:
            return all_arrival_numbers[num]

        num = iterate(num)

    return num


assert arrival_number(1, defaultdict(int)) == 1
assert arrival_number(44, defaultdict(int)) == 1
assert arrival_number(85, defaultdict(int)) == 89
assert arrival_number(89, defaultdict(int)) == 89
assert arrival_number(145, defaultdict(int)) == 89


arrival_numbers: dict[int, int] = defaultdict(int)

# For the highest starting number 9999999 -> 7 * 9^2 = 567.
# Clearly all numbers 567 < n < 9999999 will have a next iteration <= 567.
for i in range(1, 568):
    arrival_numbers[i] = arrival_number(i, arrival_numbers)

for n in range(568, 10000000):
    next_num = iterate(n)
    arrival_numbers[n] = arrival_numbers[next_num]

print(list(arrival_numbers.values()).count(89))
