import sys
from typing import List


def permutations(input: List[int]) -> List[int]:
    if len(input) < 2:
        yield input
        return
    for sub_perm in permutations(input[1:]):
        for i in range(len(input)):
            yield sub_perm[:i] + input[0:1] + sub_perm[i:]


if __name__ == "__main__":
    for p in permutations(sys.argv[1]):
    	print(p)
