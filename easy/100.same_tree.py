from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
if __name__ == "__main__":
    test_cases = [
        (TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)), True),
        (TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2)), False),
        (TreeNode(1, TreeNode(2), None), TreeNode(1, None, TreeNode(2)), False),
        (TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), None), False),
        (TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, None, TreeNode(3)), False),
        (TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(4)), False),
        (TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)), True),
        (TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4)), TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4)), True),
    ]

    for i, (p, q, expected) in enumerate(test_cases):
        result = Solution().isSameTree(p, q)
        print(f"Test {i + 1}: {p}, {q}")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")