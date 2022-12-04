from helpers import fibonacci
from itertools import takewhile

less_than_thousand_digits = takewhile(lambda fib: len(str(fib)) < 1000, fibonacci())

print(len(list(less_than_thousand_digits)) + 1)
