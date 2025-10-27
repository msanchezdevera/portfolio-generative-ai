# Bug: wrong average due to integer division

from typing import List

def average(nums: List[int]) -> float:
    if not nums:
        return 0.0
    return sum(nums) // len(nums)

if __name__ == "__main__":
    print(average([1, 2]))  # Espero 1.5, pero imprime 1
