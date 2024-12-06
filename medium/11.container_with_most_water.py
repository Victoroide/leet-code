from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            if height[left] < height[right]:
                current_area = height[left] * (right - left)
                left += 1
            else:
                current_area = height[right] * (right - left)
                right -= 1
            max_area = max(max_area, current_area)

        return max_area
    
if __name__ == "__main__":
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
    ]

    for i, (input_strs, expected) in enumerate(test_cases):
        result = Solution().maxArea(input_strs)
        print(f"Test {i + 1}: {input_strs}")
        print(f"Expected: '{expected}', Got: '{result}'")
        print("Pass" if result == expected else "Fail")
        print("-" * 50)