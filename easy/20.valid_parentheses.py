class Solution:
    def isValid(self, s: str) -> bool:
        pairs = ['()', '[]', '{}']
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] + char in pairs:
                    stack.pop()
                else:
                    return False
                
        return not stack
    
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ]

    for i, (s, expected) in enumerate(test_cases):
        result = Solution().isValid(s)
        print(f"Test {i + 1}: '{s}'")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")
        print("-" * 50)