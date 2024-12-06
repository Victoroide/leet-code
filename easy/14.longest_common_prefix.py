from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        prefix = strs[0]

        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix: return ''
                    
        return prefix
        
if __name__ == "__main__":
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interview", "interact", "interval"], "inter"),
        ([""], ""),
        ([], ""),
        (["a"], "a"),
        (["ab", "a"], "a")
    ]

    for i, (input_strs, expected) in enumerate(test_cases):
        result = Solution().longestCommonPrefix(input_strs)
        print(f"Test {i + 1}: {input_strs}")
        print(f"Expected: '{expected}', Got: '{result}'")
        print("Pass" if result == expected else "Fail")
        print("-" * 50)