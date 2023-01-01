# While it is sufficient to apply subtraction rule simplifications, this solution
# provides functions for construction and simplification of general valid roman numerals.

denominations = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def simple_roman(x: int) -> str:
    res = []
    for letter, value in denominations.items():
        while x >= value:
            res.append(letter)
            x -= value
    return "".join(res)


assert simple_roman(1) == "I"
assert simple_roman(2) == "II"
assert simple_roman(3) == "III"
assert simple_roman(4) == "IIII"
assert simple_roman(5) == "V"
assert simple_roman(6) == "VI"
assert simple_roman(10) == "X"
assert simple_roman(20) == "XX"
assert simple_roman(50) == "L"
assert simple_roman(100) == "C"
assert simple_roman(500) == "D"
assert simple_roman(999) == "DCCCCLXXXXVIIII"
assert simple_roman(1000) == "M"


def apply_subtraction_rule(numeral: str) -> str:
    return (
        numeral.replace("IIII", "IV")
        .replace("VIV", "IX")
        .replace("XXXX", "XL")
        .replace("LXL", "XC")
        .replace("CCCC", "CD")
        .replace("DCD", "CM")
    )


assert apply_subtraction_rule("I") == "I"
assert apply_subtraction_rule("VIII") == "VIII"
assert apply_subtraction_rule("IIII") == "IV"
assert apply_subtraction_rule("DCCCCLXXXX") == "CMXC"
assert apply_subtraction_rule("DCCCCLXXXXVIIII") == "CMXCIX"


def decode_roman(numeral: str) -> int:
    res = 0
    min_char = 1
    for c in numeral[::-1]:
        val = denominations[c]
        if val < min_char:
            res -= val
        else:
            res += val
            min_char = val
    return res


assert decode_roman("I") == 1
assert decode_roman("II") == 2
assert decode_roman("IIIII") == 5
assert decode_roman("V") == 5
assert decode_roman("IV") == 4
assert decode_roman("X") == 10
assert decode_roman("L") == 50
assert decode_roman("C") == 100
assert decode_roman("D") == 500
assert decode_roman("CMXCIX") == 999
assert decode_roman("M") == 1000


with open("089.txt", "r") as infile:
    numbers = [line.strip() for line in infile.readlines()]

minimal_numbers = [
    apply_subtraction_rule(simple_roman(decode_roman(line))) for line in numbers
]

charcount_initial = sum(len(num) for num in numbers)
charcount_final = sum(len(num) for num in minimal_numbers)

print(charcount_initial - charcount_final)
