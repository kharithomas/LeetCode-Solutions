from typing import Optional

from helpers.linked_list import ListNode, LinkedList, print_list

# TC : O(N)
# SC : O(1)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # find midpoint node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # reverse second half
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        first, second = head, prev

        # merge reversed half
        while second:
            temp, temp2 = first.next, second.next
            first.next = second
            second.next = temp
            first, second = temp, temp2


s = Solution()

l = LinkedList([1, 2, 3, 4])
s.reorderList(l.head)
print_list(l.head)

l2 = LinkedList([1, 2, 3, 4, 5])
s.reorderList(l2.head)
print_list(l2.head)
