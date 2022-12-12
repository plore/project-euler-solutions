from itertools import takewhile

from helpers import fibonacci

less_than_thousand_digits = takewhile(lambda fib: len(str(fib)) < 1000, fibonacci())

print(len(list(less_than_thousand_digits)) + 1)
