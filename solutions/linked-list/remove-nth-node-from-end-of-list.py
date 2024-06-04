from typing import Optional

from helpers.linked_list import ListNode, LinkedList, print_list


# TC : O(N)
# SC : O(1)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head

        for _ in range(n):
            fast = fast.next

        # corner case - remove first node
        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head


l = LinkedList([1, 2, 3, 4, 5])
print_list(l.head)

s = Solution()
s.removeNthFromEnd(l.head, n=2)

print_list(l.head)
