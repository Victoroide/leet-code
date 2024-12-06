from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return result

if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], 0, [[-1, -1, 0, 2], [-1, 0, 0, 1]]),
        ([0, 0, 0, 0], 0, [[0, 0, 0, 0]]),
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    ]

    for i, (input_strs, target, expected) in enumerate(test_cases):
        result = Solution().fourSum(input_strs, target)
        print(f"Test {i + 1}: {input_strs}, Target: {target}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")