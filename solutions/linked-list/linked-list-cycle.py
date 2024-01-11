# TC : O(N), where N is number of nodes in list
# SC : O(1)

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


s = Solution()

# Cycle List
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next
print(s.hasCycle(head))

# Normal List
head2 = ListNode(1)
head2.next = ListNode(2)
print(s.hasCycle(head2))
