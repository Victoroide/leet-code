from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
    
if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0, 0, 0], [[0, 0, 0]]),
        ([-1, 0, 1, 0], [[-1, 0, 1]]),
    ]

    for i, (input_strs, expected) in enumerate(test_cases):
        result = Solution().threeSum(input_strs)
        print(f"Test {i + 1}: {input_strs}")
        print(f"Expected: '{expected}', Got: '{result}'")
        print("Pass" if result == expected else "Fail")
        print("-" * 50)