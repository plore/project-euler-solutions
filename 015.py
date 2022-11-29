# There are fourty edges to traverse, twenty of which must be traversed from
# left to right and twenty from top to bottom. Since neither the order of
# left-to-right traversals nor the order of top-to-bottom traversals matter,
# this is equal to 40 choose 20.

from math import factorial

print(factorial(40) // factorial(20) ** 2)
