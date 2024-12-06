from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1

        return res
    
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
        ([1, 2], 3, [1, 2]),
    ]

    for i, (numbers, target, expected) in enumerate(test_cases):
        result = Solution().twoSum(numbers, target)
        print(f"Test {i + 1}: {numbers}, Target: {target}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")
        print("-" * 50)