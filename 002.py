from itertools import takewhile
from helpers import fibonacci


terms = takewhile(lambda term: term < 4000000, fibonacci())
print(sum(term for term in terms if term % 2 == 0))
