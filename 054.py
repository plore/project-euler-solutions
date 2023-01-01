from collections import Counter
from enum import IntEnum

transdict = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
    "C": 0,
    "D": 1,
    "H": 2,
    "S": 3,
}


def get_values_and_suits(cards: list[str]) -> tuple[list[int], list[int]]:
    return (
        [transdict[card[0]] for card in cards],
        [transdict[card[1]] for card in cards],
    )


class HandRank(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9


def score(cards: list[str]) -> tuple[HandRank, list[int]]:
    # pylint: disable=too-many-return-statements

    values, suits = get_values_and_suits(cards)

    values = sorted(values, reverse=True)

    freqs = Counter(values)

    match sorted(freqs.most_common(), key=lambda tup: tup[1], reverse=True):
        case [(four, 4), (one, 1)]:
            return HandRank.FOUR_OF_A_KIND, [four, one]
        case [(three, 3), (two, 2)]:
            return HandRank.FULL_HOUSE, [three, two]
        case [(three, 3), (a, 1), (b, 1)]:
            return HandRank.THREE_OF_A_KIND, [three, max(a, b), min(a, b)]
        case [(a, 2), (b, 2), (c, 1)]:
            return HandRank.TWO_PAIRS, [max(a, b), min(a, b), c]
        case [(a, 2), (b, 1), (c, 1), (d, 1)]:
            return HandRank.ONE_PAIR, [a, *sorted([b, c, d], reverse=True)]
        case _:
            straight = values[0] - values[-1] == 4
            flush = len(set(suits)) == 1

            if straight and flush:
                if values[0] == 12:
                    return HandRank.ROYAL_FLUSH, []
                return HandRank.STRAIGHT_FLUSH, [values[0]]
            if flush:
                return HandRank.FLUSH, [values[0]]
            if straight:
                return HandRank.STRAIGHT, [values[0]]

            return HandRank.HIGH_CARD, [*values]
    # pylint: disable=unpacking-non-sequence; https://github.com/PyCQA/pylint/issues/5288


assert score("5H 5C 6S 7S KD".split(" ")) == (HandRank.ONE_PAIR, [3, 11, 5, 4])
assert score("2C 3S 8S 8D TD".split(" ")) == (HandRank.ONE_PAIR, [6, 8, 1, 0])
assert score("5D 8C 9S JS AC".split(" ")) == (HandRank.HIGH_CARD, [12, 9, 7, 6, 3])
assert score("2C 5C 7D 8S QH".split(" ")) == (HandRank.HIGH_CARD, [10, 6, 5, 3, 0])
assert score("2D 9C AS AH AC".split(" ")) == (HandRank.THREE_OF_A_KIND, [12, 7, 0])
assert score("3D 6D 7D TD QD".split(" ")) == (HandRank.FLUSH, [10])
assert score("4D 6S 9H QH QC".split(" ")) == (HandRank.ONE_PAIR, [10, 7, 4, 2])
assert score("3D 6D 7H QD QS".split(" ")) == (HandRank.ONE_PAIR, [10, 5, 4, 1])
assert score("2H 2D 4C 4D 4S".split(" ")) == (HandRank.FULL_HOUSE, [2, 0])
assert score("3C 3D 3S 9S 9D".split(" ")) == (HandRank.FULL_HOUSE, [1, 7])
assert score("3C 3D 4S 4D 9D".split(" ")) == (HandRank.TWO_PAIRS, [2, 1, 7])
assert score("3C 4D 5S 6D 7D".split(" ")) == (HandRank.STRAIGHT, [5])
assert score("3C 3D 3S 3H 7D".split(" ")) == (HandRank.FOUR_OF_A_KIND, [1, 5])
assert score("3D 4D 5D 6D 7D".split(" ")) == (HandRank.STRAIGHT_FLUSH, [5])
assert score("TD JD QD KD AD".split(" ")) == (HandRank.ROYAL_FLUSH, [])

with open("054.txt", "r") as infile:
    hands = [line.strip().split(" ") for line in infile]


def one_wins(values1: list[int], values2: list[int]) -> bool:
    for val1, val2 in zip(values1, values2):
        if val1 > val2:
            return True
        if val1 < val2:
            return False
    return False


wins_player_one = 0
for all_cards in hands:
    hand_one, hand_two = all_cards[:5], all_cards[5:]
    rank_one, values_one = score(hand_one)
    rank_two, values_two = score(hand_two)
    if rank_one > rank_two or (
        rank_one == rank_two and one_wins(values_one, values_two)
    ):
        wins_player_one += 1

print(wins_player_one)
