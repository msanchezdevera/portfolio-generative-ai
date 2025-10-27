from typing import List

def average(nums: List[int]) -> float:
    if not nums:
        return 0.0
    return sum(nums) / len(nums)  # Changed from // to /

def test_average():
    """Micro-tests for average function"""
    # Test case 1: [1,2] -> 1.5
    assert average([1, 2]) == 1.5, f"Expected 1.5, got {average([1, 2])}"
    
    # Test case 2: [3,3,3] -> 3.0
    assert average([3, 3, 3]) == 3.0, f"Expected 3.0, got {average([3, 3, 3])}"
    
    # Test case 3: [] -> 0.0
    assert average([]) == 0.0, f"Expected 0.0, got {average([])}"
    
    print("All tests passed!")

if __name__ == "__main__":
    print(average([1, 2]))  # Now correctly prints 1.5
    test_average()