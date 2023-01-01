# mypy can't infer enum values
# mypy: disable-error-code=attr-defined
from enum import IntEnum
from random import randint, sample

fields: list[str] = (
    ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3"]
    + ["JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3"]
    + ["FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3"]
    + ["G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]
)
Field = IntEnum("Field", fields, start=0)  # type: ignore

cards_CC = ["GO", "G2J"] + ["STAY"] * 14

cards_CH = ["GO", "G2J", "C1", "E3", "H2", "R1", "nextR", "nextR", "nextU", "back3"] + [
    "STAY"
] * 6


def nextR(pos: int) -> int:
    if 5 < pos <= 15:
        return 15
    if 15 < pos <= 25:
        return 25
    if 25 < pos <= 35:
        return 35
    return 5


def nextU(pos: int) -> int:
    if 12 < pos <= 28:
        return 28
    return 12


def back3(pos: int) -> int:
    res = pos - 3
    if res < 0:
        res += len(Field)
    return res


def apply_effect(pos: int, index_CC: int, index_CH: int) -> tuple[int, int, int]:
    if pos == Field.G2J:
        return Field.JAIL, index_CC, index_CH
    if pos in (Field.CC1, Field.CC2, Field.CC3):
        new_pos = {
            "GO": Field.GO,
            "G2J": Field.JAIL,
            "STAY": pos,
        }[cards_CC[index_CC]]
        return new_pos, (index_CC + 1) % len(cards_CC), index_CH
    if pos in (Field.CH1, Field.CH2, Field.CH3):
        new_pos = {
            "GO": Field.GO,
            "G2J": Field.JAIL,
            "C1": Field.C1,
            "E3": Field.E3,
            "H2": Field.H2,
            "R1": Field.R1,
            "nextR": nextR(pos),
            "nextU": nextU(pos),
            "back3": back3(pos),
            "STAY": pos,
        }[cards_CH[index_CH]]
        return new_pos, index_CC, (index_CH + 1) % len(cards_CH)
    return pos, index_CC, index_CH


assert apply_effect(Field.GO, 0, 0) == (Field.GO, 0, 0)
assert apply_effect(Field.A1, 0, 0) == (Field.A1, 0, 0)
assert apply_effect(Field.G2J, 0, 0) == (Field.JAIL, 0, 0)

assert apply_effect(Field.CC1, 0, 0) == (Field.GO, 1, 0)
assert apply_effect(Field.CC2, 1, 0) == (Field.JAIL, 2, 0)
assert apply_effect(Field.CC3, 2, 0) == (Field.CC3, 3, 0)
assert apply_effect(Field.CC1, 15, 0) == (Field.CC1, 0, 0)

assert apply_effect(Field.CH1, 0, 0) == (Field.GO, 0, 1)
assert apply_effect(Field.CH2, 0, 1) == (Field.JAIL, 0, 2)
assert apply_effect(Field.CH3, 0, 2) == (Field.C1, 0, 3)
assert apply_effect(Field.CH1, 0, 3) == (Field.E3, 0, 4)
assert apply_effect(Field.CH2, 0, 4) == (Field.H2, 0, 5)
assert apply_effect(Field.CH3, 0, 5) == (Field.R1, 0, 6)
assert apply_effect(Field.CH1, 0, 6) == (Field.R2, 0, 7)
assert apply_effect(Field.CH2, 0, 7) == (Field.R3, 0, 8)
assert apply_effect(Field.CH3, 0, 8) == (Field.U1, 0, 9)
assert apply_effect(Field.CH1, 0, 9) == (Field.T1, 0, 10)
assert apply_effect(Field.CH2, 0, 10) == (Field.CH2, 0, 11)
assert apply_effect(Field.CH2, 0, 15) == (Field.CH2, 0, 0)


dice_sides = 4
num_turns = 2000
num_plays = 2000

freqs = [0] * len(Field)
consecutive_doubles = 0

for _ in range(num_plays):
    cards_CC = sample(cards_CC, k=len(cards_CC))
    cards_CH = sample(cards_CH, k=len(cards_CH))
    position = idx_CC = idx_CH = 0
    for _ in range(num_turns):
        dice1 = randint(1, dice_sides)
        dice2 = randint(1, dice_sides)

        consecutive_doubles = consecutive_doubles + 1 if dice1 == dice2 else 0
        if consecutive_doubles == 3:
            position = Field.JAIL
            consecutive_doubles = 0
        else:
            position = (position + dice1 + dice2) % len(Field)
            position, idx_CC, idx_CH = apply_effect(position, idx_CC, idx_CH)
        freqs[position] += 1

sorted_frequencies = sorted(enumerate(freqs), key=lambda tup: tup[1], reverse=True)
top3_popular_squares = [f"{index:02}" for index, freq in sorted_frequencies[:3]]
print("".join(top3_popular_squares))
