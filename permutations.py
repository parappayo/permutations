import sys
from typing import List


def permutations(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        yield nums
        return
    for sub_perm in permutations(nums[1:]):
        for i in range(len(nums)):
            yield sub_perm[:i] + nums[0:1] + sub_perm[i:]


if __name__ == "__main__":
    for p in permutations(sys.argv[1]):
    	print(p)
