from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            
        return len(nums)

if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([], 5, 0),
        ([1], 0, 0),
        ([1], 2, 1)
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = Solution().searchInsert(nums, target)
        print(f"Test {i + 1}: nums={nums}, target={target}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")
        print("-" * 50)