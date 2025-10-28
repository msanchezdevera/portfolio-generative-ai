from typing import List

def compute_stats(nums: List[float]):
    if not nums:
        return None
    mn = nums[0]
    mx = nums[0]
    s = 0.0
    for x in nums:
        if x < mn: mn = x
        if x > mx: mx = x
        s += x
    return mn, mx, s/len(nums)
