from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        self.dfs(digits, mapping, 0, '', result)
        return result
    
    def dfs(self, digits, mapping, index, path, result):
        if index == len(digits):
            result.append(path)
            return
        
        for char in mapping[digits[index]]:
            print("Before DFS: ", result)
            self.dfs(digits, mapping, index + 1, path + char, result)
            print("After DFS: ", result)

if __name__ == "__main__":
    test_cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"])
    ]

    for i, (digits, expected) in enumerate(test_cases):
        result = Solution().letterCombinations(digits)
        print(f"Test {i + 1}: '{digits}'")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")
        print("-" * 50)