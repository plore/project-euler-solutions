from itertools import takewhile
from typing import Generator

def fibonacci() -> Generator[int, None, None]:
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

terms = takewhile(lambda term: term < 4000000, fibonacci())
print(sum(term for term in terms if term % 2 == 0))
