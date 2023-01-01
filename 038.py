# 918273645 = 9 * (1,2,3,4,5) is the highest possible concatenated product starting from
# a single digit integer.
# To get to higher concatenated products the base number needs to be of the form 9<rest>
# Base numbers of five digits can be exluded since 9#### * (1, 2) would contain eleven
# digits (9####1+++++).
# Two-digit base numbers lead to 9# * (1,2,3) = 9#1aa2bb or 9# * (1,2,3,4) = 9#1aa2bb3cc
# of 8 or 11 digits, respectively.
# Three-digit base numbers lead to 9## * (1,2) = 9##1aaa or 9## * (1,2,3) = 9##1aaa2bbb
# of 7 or 11 digits, respectively.
# Thus, search through 4-digit base numbers 9### * (1, 2) = 9###1++++ only.

for p in range(9876, 9000, -1):
    concat = f"{p}{p*2}"
    if all(digit in concat for digit in "123456789"):
        print(concat)
        break
