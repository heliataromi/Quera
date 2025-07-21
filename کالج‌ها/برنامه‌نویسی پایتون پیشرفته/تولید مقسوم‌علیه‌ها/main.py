from typing import Generator

def divs(n: int) -> Generator[int, None, None]:
    for i in range(1, n + 1):
        if n % i == 0:
            yield i
