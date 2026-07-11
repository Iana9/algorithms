from dataclasses import dataclass
from typing import List


@dataclass
class Result:
    min: int
    max: int


def findMinMax(lst: List[int]) -> Result:
    min_val: int = lst[0]
    max_val: int = lst[0]
    for i in range(1, len(lst)):
        if min_val > lst[i]:
            min_val = lst[i]
        if max_val < lst[i]:
            max_val = lst[i]
    return Result(min_val, max_val)


def _pair_min_max(a: int, b: int) -> tuple[int, int]:
    if a < b:
        return a, b
    return b, a


def findMinMax2(lst: List[int]) -> Result:
    n = len(lst)
    if n == 1:
        return Result(lst[0], lst[0])

    if n % 2 == 1:
        min_val = max_val = lst[0]
        start = 1
    else:
        min_val, max_val = _pair_min_max(lst[0], lst[1])
        start = 2

    for i in range(start, n, 2):
        local_min, local_max = _pair_min_max(lst[i], lst[i + 1])
        if local_min < min_val:
            min_val = local_min
        if local_max > max_val:
            max_val = local_max

    return Result(min_val, max_val)