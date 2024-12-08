from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        for _ in range(n + 1):
            first = first.next
            
        while first:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        return dummy.next
    
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
    ]

    for i, (input_list, n, expected_list) in enumerate(test_cases):
        head = ListNode(input_list[0])
        current = head
        for val in input_list[1:]:
            current.next = ListNode(val)
            current = current.next

        result = Solution().removeNthFromEnd(head, n)
        result_list = []
        while result:
            result_list.append(result.val)
            result = result.next

        print(f"Test {i + 1}: {input_list} -> {n}")
        print(f"Expected: {expected_list}, Got: {result_list}")
        print("Pass" if expected_list == result_list else "Fail")
        print("-" * 50)