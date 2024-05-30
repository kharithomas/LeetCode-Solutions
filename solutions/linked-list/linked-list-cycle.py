from typing import Optional

from helpers.linked_list import ListNode


# TC : O(N)
# SC : O(1)


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
